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

1. Created a function `url_response(url)` to send an HTTP `HEAD` request to each URL.

- Printed the status code if the request was successful.
- Handled exceptions by printing "(Not found)" for unreachable URLs.

2. Opened the csv file with UTF-8 encoding.

- Used the built-in csv.reader() to parse the file.
- Skipped the header row using next(reader).

3. Used `ThreadPoolExecutor` to handle multiple URL requests in parallel.

- Applied `executor.map()` to execute the `url_response()` function on all extracted URLs.

4. Printed each URL along with its corresponding status code.
