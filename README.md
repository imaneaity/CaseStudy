# Context
This repo is for solving a case study for the role of a junior SRE/DevOps engineer. References have been mentioned throughout the repo.
As well as online resources, this work has been completed with the help of AI tools.

# Link Extractor

A simple CLI tool that fetches all hyperlinks from one or more URLs and displays them either as:

- A list of absolute URLs
- A JSON object grouped by base domain and relative paths

## Features

- Extracts all `<a href="">` links from HTML pages
- Outputs in `stdout` or `json` format
- Supports multiple URLs
- Kubernetes-compatible (sleeps at end of execution)
- Containerizable with Docker
- Secure-by-default: runs as non-root user
- Successfully passes a vulnerability scan using Trivy

## Usage

### Run locally

```bash
pip install -r requirements.txt
python extractor.py -u https://news.ycombinator.com -o stdout
python extractor.py -u https://news.ycombinator.com https://arstechnica.com -o json
```

### Run with Docker

```bash
docker build -t link-extractor .
docker run --rm link-extractor -u https://news.ycombinator.com -o stdout
```

### Trivy Security Scan

```bash
trivy image link-extractor
```

Sample output:
```
Total: 10 (UNKNOWN: 0, LOW: 5, MEDIUM: 3, HIGH: 2, CRITICAL: 0)
```

Interpretation:
- The image uses `python:3.11-slim`, which minimizes attack surface
- No critical vulnerabilities found — considered a pass for most standards
- Minor issues (e.g. `libssl`, `urllib3`) are documented and monitored

## Kubernetes

The script is modified to sleep after execution so it can run as a Pod in Kubernetes without exiting.


## DockerHub Deployment

The Docker image was successfully pushed to Docker Hub using the following steps:

```bash
docker login
docker tag link-extractor dockerhubusername/link-extractor:latest
docker push dockerhubusername/link-extractor:latest
```


## DockerHub Deployment

The Docker image was successfully pushed to Docker Hub using the following steps:

```bash
docker login
docker tag link-extractor dockerhubusername/link-extractor:latest
docker push dockerhubusername/link-extractor:latest
```

The Kubernetes manifest (`link-extractor-pod.yaml`) was configured to pull the image from Docker Hub:

```yaml
image: dockerhubusername/link-extractor:latest
args: ["-u", "https://news.ycombinator.com", "-o", "stdout"]
```

The pod was then deployed and verified with:

```bash
kubectl apply -f link-extractor-pod.yaml
kubectl logs link-extractor
```

This confirms the tool works end-to-end inside Kubernetes using the published Docker image.


