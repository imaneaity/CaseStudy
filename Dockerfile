# Use a minimal base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy source code and dependencies
COPY extractor.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Add non-root user
RUN useradd -m appuser
USER appuser

# Entry point with CLI args
ENTRYPOINT ["python", "extractor.py"]
