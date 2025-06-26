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


## CI/CD Pipeline with GitHub Actions

A GitHub Actions workflow is set up to:
- Build the Docker image
- Push it to DockerHub
- Scan it with Trivy for vulnerabilities

### Secrets Required
Add the following secrets to your GitHub repo under:
**Settings > Secrets and variables > Actions**

| Name              | Description              |
|-------------------|--------------------------|
| DOCKER_USERNAME   | Your DockerHub username  |
| DOCKER_PASSWORD   | Your DockerHub password or token |

### Trigger
The pipeline runs automatically on every push to the `master` branch.

Workflow file: `.github/workflows/ci-cd.yml`

## Part 3 Reference

A detailed write-up of the CI/CD pipeline and its screenshots is available in:
`Part3-pipeline.md`

---

## Part 4 – Domain Extraction with Shell Tools

This part focuses on using Unix tools like `awk`, `tr`, `sed`, and `grep` to clean and normalize domain names from a text file.

### Example Input (`input.txt`)

```
http://tiktok.com
https://ads.faceBook.com.
https://sub.ads.faCebook.com
api.tiktok.com
Google.com.
aws.amazon.com
```

### Expected Output

```
tiktok.com
facebook.com
google.com
amazon.com
```

### How to Run

1. Ensure `input.txt` contains the sample URLs.
2. Run the script:

```bash
chmod +x domain_extraction.sh
./domain_extraction.sh
```

Both methods will extract the main domain names, normalize them to lowercase, and remove duplicates.

