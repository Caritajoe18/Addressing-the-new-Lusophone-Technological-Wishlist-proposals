import requests, csv, re
from concurrent.futures import ThreadPoolExecutor

# Define regex pattern for extracting URLs
url_pattern = re.compile(r'https?://[^\s]+')

def url_response(url):
    """Send a HEAD request and print the status code."""
    try:
        print(f"({requests.head(url, allow_redirects=True, timeout=10).status_code}) {url}")
    except requests.RequestException:
        print(f"(Not found) {url}")

# Extract URLs using regex from CSV file
with open("Task 2 - Intern.csv", encoding='utf-8') as f:
    urls = [match for row in csv.reader(f) for match in url_pattern.findall(row[0])]  

# Process URLs concurrently
with ThreadPoolExecutor() as executor:
    executor.map(url_response, urls)
