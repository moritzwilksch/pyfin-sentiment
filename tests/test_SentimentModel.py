import numpy as np
import pytest

from pyfin_sentiment.model import SentimentModel

SentimentModel.download("small")
model = SentimentModel("small")


@pytest.mark.parametrize(
    "text, prediction",
    [
        ("long $AAPL", "1"),
        ("short $TSLA", "3"),
        ("Join our chatroom!", "2"),
    ],
)
def test_predict(text: str, prediction: str):
    pred = model.predict([text])
    assert pred == np.array([prediction])


@pytest.mark.parametrize(
    "fn_input, exception",
    [
        ([], ValueError),
        ("", ValueError),
    ],
)
def test_predict_throws_exception(fn_input, exception):
    with pytest.raises(exception):
        model.predict(fn_input)


@pytest.mark.parametrize(
    "text",
    [
        ("long $AAPL"),
        ("short $TSLA"),
        ("Join our chatroom!"),
    ],
)
def test_predict_proba(text: str):
    pred = model.predict_proba([text])
    assert pred.shape == (1, 3)
    np.testing.assert_array_almost_equal(
        pred.sum(axis=1), np.array([1.0]), verbose=True
    )
