# <img align="right" width=64 src="https://user-images.githubusercontent.com/58488209/167823474-1e756f0e-8ede-49bf-8d4b-5b470fddd43d.png"> pyFin-Sentiment

[![Documentation Status](https://readthedocs.org/projects/pyfin-sentiment/badge/?version=latest)](https://pyfin-sentiment.readthedocs.io/en/latest/?badge=latest)
[![CI (tests)](https://github.com/moritzwilksch/pyfin-sentiment/actions/workflows/main.yml/badge.svg)](https://github.com/moritzwilksch/pyfin-sentiment/actions/workflows/main.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A library for sentiment analysis of financial social media posts

**IMPORTANT: This library is a WIP. Expect completion by September 2022 :)**

## Sentiment Analysis of Financial Social Media Posts
*This section is a WIP*

## Example
```python
from pyfin_sentiment.model import SentimentModel

# this only needs to be downloaded once:
SentimentModel.download("small")  # downloads to ~/.cache/python-sentiment

model = SentimentModel("small")
model.predict(["Long $TSLA!!", "Selling my $AAPL position"])
# array(['1', '3'], dtype=object)
```

## Documentation
> 📚 The documentation lives on [pyfin-sentiment.readthedocs.io](https://pyfin-sentiment.readthedocs.io/en/latest)



## Citation
If you use the library, please cite it:

> Wilksch, M. (2022). pyFin-Sentiment: a library for sentiment analysis of financial social media posts. `https://github.com/moritzwilksch/pyfin-sentiment`


```latex
@misc{pyfin-sentiment,
  author={Wilksch, Moritz},
  title={pyFin-Sentiment: a library for sentiment analysis of financial social media posts},
  year={2022},
  howpublished={\url{https://github.com/moritzwilksch/pyfin-sentiment}}
}
```
