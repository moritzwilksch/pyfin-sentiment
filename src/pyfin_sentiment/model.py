import os
import pathlib
import urllib.request
from typing import Union

import joblib
import numpy as np
import polars as pl

from pyfin_sentiment.preprocessing import Preprocessor


class SentimentModel:
    """
    The pyFin-sentiment model class. Use this to download the model with `SentimentModel.download(...)` and instanciate it using `SentimentModel(model_name)`.

    Raises:
        ValueError: When you try to instanciate a model that does not exist.
        FileNotFoundError: When your cache directory does not exist or is not writable.
    """

    # list of all available models
    AVAILABLE_MODELS = ["small"]

    # remote locations for the models
    SMALL_MODEL_LOCATION = "https://pyfin-sentiment.s3.us-west-004.backblazeb2.com/final_LogisticRegressionModel.gz"

    # mapping of model names to file names/remote locations
    NAME_FILE_MAPPING = {"small": "small.gz"}
    NAME_LOCATION_MAPPING = {"small": SMALL_MODEL_LOCATION}

    def __init__(self, model_name: str = "small", cache_dir: str = None):
        """
        Initialize a pyFin-sentiment model by name. The model artifact needs to be downloaded first using `SentimentModel.download(model_name)`.

        Args:
            model_name (str, optional): Model name, one of: ["small"]. Valid names are also listed in SentimentModel.AVAILABLE_MODELS. Defaults to "small".
            cache_dir (str, optional): Directory in which model artifacts are located. Defaults to ~/.cache/pyfin-sentiment.

        Raises:
            ValueError: When you try to instanciate a model that does not exist.

        Tip:
            If downloading or loading the model fails with the implicit cache_dir, try setting cache_dir to a writable directory that already exists.
        """

        if model_name not in self.AVAILABLE_MODELS:
            raise ValueError(
                f"Model {model_name} is not available. Use one of: {self.AVAILABLE_MODELS}"
            )

        if cache_dir is None:
            self.cache_dir = self._create_get_cache_dir()
        else:
            self.cache_dir = pathlib.Path(cache_dir)

        # path to model file
        model_path = self.cache_dir / self.NAME_FILE_MAPPING[model_name]

        self.model = joblib.load(model_path)
        self.preprocessor = Preprocessor()

    @staticmethod
    def _create_get_cache_dir():
        """
        Get path to default cache directory. Tries to create `~/.cache/pyfin-sentiment` if it does not exist.

        Returns:
            pathlib.Path: Path to cache directory.
        """
        # pyfin-sentiment cache exists
        if (pathlib.Path().home() / ".cache" / "pyfin-sentiment").exists():
            return pathlib.Path().home() / ".cache" / "pyfin-sentiment"
        # ~/.cache exists, but pyfing-sentiment needs to be created
        elif (pathlib.Path().home() / ".cache").exists():
            try:
                os.mkdir(pathlib.Path().home() / ".cache" / "pyfin-sentiment")
                return pathlib.Path().home() / ".cache" / "pyfin-sentiment"
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not create the cache directory {pathlib.Path().home() / '.cache' / 'pyfin-sentiment'}. Do you have the right permissions? If not, try passing an exisiting directory to `cache_dir`."
                )
        # ~/.cache does not exist, try creating it
        else:
            try:
                os.mkdir(pathlib.Path().home() / ".cache")
                os.mkdir(pathlib.Path().home() / ".cache" / "pyfin-sentiment")
                return pathlib.Path().home() / ".cache" / "pyfin-sentiment"
            except FileNotFoundError:
                raise FileNotFoundError(
                    f"Could not create the cache directory {pathlib.Path().home() / '.cache'}. Do you have the right permissions? If not, try passing an exisiting directory to `cache_dir`."
                )

    @classmethod
    def download(cls, model_name: str = "small", cache_dir: str = None):
        """
        Download the model artifact into `cache_dir`.

        Args:
            model_name (str, optional): Model name, one of: ["small"]. Valid names are also listed in SentimentModel.AVAILABLE_MODELS. Defaults to "small".
            cache_dir (str, optional): Directory to which model artifacts are saved. Defaults to ~/.cache/pyfin-sentiment.
        """

        if cache_dir is None:
            cache_dir = cls._create_get_cache_dir()
        else:
            cache_dir = pathlib.Path(cache_dir)

        if (cache_dir / cls.NAME_FILE_MAPPING[model_name]).exists():
            print(
                f"Model {model_name} already exists in location {cache_dir}, skipping download."
            )
            return

        urllib.request.urlretrieve(
            cls.NAME_LOCATION_MAPPING[model_name],
            cache_dir / cls.NAME_FILE_MAPPING[model_name],
        )

        print(f"Model downloaded to {cache_dir / cls.NAME_FILE_MAPPING[model_name]}")

    def predict(self, texts: Union[list, np.ndarray]) -> np.ndarray:
        """
        Predict sentiment class from raw texts. No prior preprocessing is necessary as it will be done internally.

        Args:
            texts (Union[list, np.ndarray]): Input texts

        Returns:
            np.ndarray: Predicted sentiment class for each text. "1" = positive, "2" = neutral, "3" = negative.
        """
        if not (isinstance(texts, list) or isinstance(texts, np.ndarray)):
            raise ValueError(
                f"Please provide a list or np.ndarray of texts. Got {type(texts)}."
            )

        if len(texts) == 0:
            raise ValueError(f"Please provide at least one text. Got {texts}")

        df = pl.DataFrame(texts, schema=["text"])
        df = self.preprocessor.process(df)

        return self.model.predict(df["text"].to_list())

    def predict_proba(self, texts: Union[list, np.ndarray]) -> np.ndarray:
        """
        Predict sentiment class probabilites from raw texts. No prior preprocessing is necessary as it will be done internally.

        Args:
            texts (Union[list, np.ndarray]): Input texts

        Returns:
            np.ndarray: Predicted sentiment class probabilities p for each text. p[:, 0] = positive, p[:, 1] = neutral, p[:, 2] = negative.
        """
        if not isinstance(texts, list) or isinstance(texts, np.ndarray):
            raise ValueError(
                f"Please provide a list or np.ndarray of texts. Got {type(texts)}."
            )

        df = pl.DataFrame(texts, schema=["text"])
        df = self.preprocessor.process(df)

        return self.model.predict_proba(df["text"].to_list())
