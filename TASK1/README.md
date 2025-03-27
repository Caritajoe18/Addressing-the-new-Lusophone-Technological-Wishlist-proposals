# Steps Taken

1. Wrote a function to convert the date into a readable format using `toLocaleDateString`.
2. Iterated through the array of data objects using the `map` function.
   - Extracted the `title`, `page_id`, and `creation_date` from each object using destructuring.
   - Used the ASCII character codes to add an alphabetical bullet point (A, B, C, etc.) to each entry.
   - Formatted the `creation_date` using the `formattedDate` function.
3. Structured the extracted data into a readable sentence.
4. Appended the formatted results to the results paragraph.
5. Ensured each entry is displayed on a separate line by using `<br>` for proper HTML formatting.
