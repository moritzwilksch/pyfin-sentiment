# 👋 Welcome to the `pyFin-Sentiment` docs!

## Before you start...
- This library is intended for extracting financial *market* sentiment from short-form social media posts like tweets. 
- Market sentiment is different from general sentiment:
> **Example:** "My $AAPL short is going great!" has a *positive* generic sentiment but a *negative* market sentiment
- If you are looking for a generic sentiment model that works well on social media content, take a look at [VADER](https://github.com/cjhutto/vaderSentiment) or [TwitterRoBERTa](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)
- If you are looking for a sentiment analysis models that excels on new headlines sentiment analysis, check out [FinBERT](https://huggingface.co/ProsusAI/finbert)
- Otherwise, stay here 🙃

We use the following conventions for mapping sentiment classes:

| Class Name | Meaning |
| --- | --- |
|1| Positive, Bullish |
|2| Neutral, Uncertain |
|3| Negative, Bearish |

## MWE
A minimum working example for the impatient:
```python
from pyfin_sentiment.model import SentimentModel

# this only needs to be downloaded once:
SentimentModel.download("small")  # downloads to ~/.cache/python-sentiment

model = SentimentModel("small")
model.predict(["Long $TSLA!!", "Selling my $AAPL position"])
# array(['1', '3'], dtype=object)

```

## The `SentimentModel` class
There's actually only one class you'll really need: the [SentimentModel](SentimentModel.md) class

