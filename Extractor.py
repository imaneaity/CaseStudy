# Link Extractor Script for SRE/DevOps Junior Case Study
# Inspired by common BeautifulSoup usage patterns from StackOverflow and official documentation
# References:
# - https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# - https://stackoverflow.com/questions/328356/extracting-all-links-from-html-using-beautifulsoup

import argparse  # For parsing command-line arguments
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
from urllib.parse import urljoin, urlparse  # For handling and normalizing URLs
import json  # For outputting JSON format
import time  # For keeping the container alive in Kubernetes

def extract_links(url):
    """
    Fetches the content of a URL and extracts all <a href=""> links as absolute URLs.
    Returns a list of those URLs.
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Join relative links to the base URL to form absolute URLs
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Extract links from given URLs.')
    parser.add_argument('-u', '--urls', nargs='+', required=True, help='HTTP URLs to fetch')
    parser.add_argument('-o', '--output', choices=['stdout', 'json'], required=True, help='Output format')
    args = parser.parse_args()

    # Output as plain list of absolute URLs
    if args.output == 'stdout':
        for url in args.urls:
            for link in extract_links(url):
                print(link)
    
    # Output as JSON grouped by base domain with relative paths
    else:
        output = {}
        for url in args.urls:
            parsed = urlparse(url)
            base = f"{parsed.scheme}://{parsed.netloc}"
            if base not in output:
                output[base] = []
            for link in extract_links(url):
                rel_path = urlparse(link).path
                output[base].append(rel_path)
        print(json.dumps(output, indent=2))

    # Keeps the container alive when running in Kubernetes
    time.sleep(1e6)

if __name__ == "__main__":
    main()
