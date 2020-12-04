# 🏠🕵️‍♂️ Flat finder

## Installation

```sh
pip install -r requirements.txt
```

Install Tesseract (used for OCR)

```sh
brew install tesseract
```

## Getting Started

Paste a URL into the `search_urls` array and run:

```sh
python main.py
```

It will produce a `properties.csv` file for any matching properties

## Tests

```
pytest
```

## TODO

- Rightmove scraper
- Zoopla scraper
- Pass URL and config options via CLI
- Store results in DB to skip double-checking
- Link properties from multiple agencies?
- Input form to gather requirements, search sources directly
