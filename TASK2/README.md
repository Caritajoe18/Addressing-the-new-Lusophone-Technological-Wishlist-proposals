# Steps Taken

## 1. Extracting URLs
- Used a regex pattern to extract HTTP and HTTPS URLs from the CSV file.

## 2. Checking URL Status
- Sent an HTTP HEAD request to each URL and printed the status code or an error message.

## 3. Processing URLs Concurrently
- Used a thread pool executor to process multiple URLs in parallel for efficiency.

## 4. Printing Results
- Displayed the status code with each URL for quick analysis.

