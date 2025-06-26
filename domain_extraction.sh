#!/bin/bash

# Extract base domains, normalize case, and remove duplicates

INPUT_FILE="input.txt"

echo "Running Solution 1 (awk + tr + sed):"
cat "$INPUT_FILE" | \
  tr 'A-Z' 'a-z' | \
  sed 's|https\?://||' | \
  sed 's/\.$//' | \
  awk -F. '{print $(NF-1)"."$NF}' | \
  sort -u



echo -e "\nRunning Solution 2 (grep + awk):"
grep -oE '([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}' "$INPUT_FILE" | \
  tr 'A-Z' 'a-z' | \
  awk -F. '{print $(NF-1)"."$NF}' | \
  sort -u
