# 👋 Welcome to the `pyFin-Sentiment` docs!

## Installation

This library requires `python>=3.8`!

```bash
pip install pyfin-sentiment
```

## Before you start...
- This library is intended for extracting financial *market* sentiment from short-form social media posts like tweets. 
- Market sentiment is different from general sentiment:
> **Example:** "My $AAPL short is going great!" has a *positive* generic sentiment but a *negative* market sentiment
- If you are looking for a generic sentiment model that works well on social media content, take a look at [VADER](https://github.com/cjhutto/vaderSentiment) or [TwitterRoBERTa](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
- If you are looking for a sentiment analysis models that excels on new headlines sentiment analysis, check out [FinBERT](https://huggingface.co/ProsusAI/finbert)
- Otherwise, stay here 🙃


### Sentiment Labels
We use the following conventions for mapping sentiment classes:

| Class Name | Meaning |
| --- | --- |
|1| Positive, Bullish |
|2| Neutral, Uncertain |
|3| Negative, Bearish |

### Models

For now, we support the following models. You'll need to specify the correct `model_name` when downloading and loading models.

| `model_name` | Description |
| --- | ---
| `"small"` (default) | A logistic regression trained on the TF-IDF representation of the sub-word tokenized texts |

## MWE
A minimum working example for the impatient:
```python
from pyfin_sentiment.model import SentimentModel

# this only needs to be downloaded once:
SentimentModel.download("small")

model = SentimentModel("small")
model.predict(["Long $TSLA!!", "Selling my $AAPL position"])
# array(['1', '3'], dtype=object)

```

## The `SentimentModel` class
There's actually only one class you'll really need: the [SentimentModel](SentimentModel.md) class


## About
This library was developed by [me (Moritz Wilksch)](https://github.com/moritzwilksch) as part of my master thesis. If you experience any issues feel free to raise them at [the project's GitHub repo](https://github.com/moritzwilksch/pyfin-sentiment).