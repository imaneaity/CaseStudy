import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import time

def extract_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description='Extract links from given URLs.')
    parser.add_argument('-u', '--urls', nargs='+', required=True, help='HTTP URLs to fetch')
    parser.add_argument('-o', '--output', choices=['stdout', 'json'], required=True, help='Output format')
    args = parser.parse_args()

    if args.output == 'stdout':
        for url in args.urls:
            for link in extract_links(url):
                print(link)
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
