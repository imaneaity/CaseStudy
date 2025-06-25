# Link Extractor

A simple CLI tool that fetches all hyperlinks from one or more URLs and displays them either as:

- A list of absolute URLs
- A JSON object grouped by base domain and relative paths

## Features

- Extracts all `<a href="">` links from HTML pages
- Outputs in `stdout` or `json` format
- Supports multiple URLs
- Containerizable with Docker

## Usage

### Run locally

```bash
pip install -r requirements.txt
python extractor.py -u https://news.ycombinator.com -o stdout
python extractor.py -u https://news.ycombinator.com https://arstechnica.com -o json
```


