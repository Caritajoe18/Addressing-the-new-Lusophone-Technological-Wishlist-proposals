## Running the Python Script

1. Clone the repository and navigate into it:
   ```sh
   git clone https://github.com/Caritajoe18/Addressing-the-new-Lusophone-Technological-Wishlist-proposals.git
   ```
   ```sh
   cd Addressing-the-new-Lusophone-Technological-Wishlist-proposals
   ```
2. From the repository folder,navigate into the Python script folder:
   ```sh
   cd TASK2
   ```
3. Run the script:
   ```sh
   python3 intern.py
   ```

# Steps Taken

## 1. Extracting URLs

- Used a regex pattern to extract HTTP and HTTPS URLs from the CSV file.

## 2. Checking URL Status

- Sent an HTTP HEAD request to each URL and printed the status code or an error message.

## 3. Processing URLs Concurrently

- Used a thread pool executor to process multiple URLs in parallel for efficiency.

## 4. Printing Results

- Displayed the status code with each URL for quick analysis.
