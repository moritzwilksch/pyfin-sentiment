# <img align="right" width=64 src="https://user-images.githubusercontent.com/58488209/167823474-1e756f0e-8ede-49bf-8d4b-5b470fddd43d.png"> pyFin-Sentiment

[![Documentation Status](https://readthedocs.org/projects/pyfin-sentiment/badge/?version=latest)](https://pyfin-sentiment.readthedocs.io/en/latest/?badge=latest)
[![CI (tests)](https://github.com/moritzwilksch/pyfin-sentiment/actions/workflows/main.yml/badge.svg)](https://github.com/moritzwilksch/pyfin-sentiment/actions/workflows/main.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A library for sentiment analysis of financial social media posts

## Sentiment Analysis of Financial Social Media Posts
This library can help you **extract market sentiment from short social media posts**. Trained on data from Twitter, it can classify sentimetn into **three classes: Bullish, Bearish, Neutral/No Sentiment**.
Note that we need to differentiate between market sentiment and general sentiment. Consider this example:

> 💬 Nice, already made loads of money this morning and now im shorting $AAPL, let's goooo!

While the general sentiment in the text is positve, the *market sentiment* is negative as the author is shorting a stock.
Therefore, ...
- If you are looking for a generic sentiment model that works well on social media content, take a look at [VADER](https://github.com/cjhutto/vaderSentiment) or [TwitterRoBERTa](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
- If you are looking for a sentiment analysis models that excels on new headlines sentiment analysis, check out [FinBERT](https://huggingface.co/ProsusAI/finbert)
- Otherwise, stay here 🙃

## Installation
It's as easy as...
```bash
pip install pyfin-sentiment
```

## Documentation
> 📚 The documentation lives on [pyfin-sentiment.readthedocs.io](https://pyfin-sentiment.readthedocs.io/en/latest)

## Example
```python
from pyfin_sentiment.model import SentimentModel

# the model only needs to be downloaded once
SentimentModel.download("small")

model = SentimentModel("small")
model.predict(["Long $TSLA!!", "Selling my $AAPL position"])
# array(['1', '3'], dtype=object)
```
We use the following conventions for mapping sentiment classes:

| Class Name | Meaning |
| --- | --- |
|1| Positive, Bullish |
|2| Neutral, Uncertain |
|3| Negative, Bearish |


