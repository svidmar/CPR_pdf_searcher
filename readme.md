
# Documentation for CPR Number Finder Script

## Overview

This script is designed to scan through PDF files within a specified directory, identifying and logging Danish Personal Identification numbers (CPR numbers). These numbers follow a specific format, either "DDMMYY-XXXX" or "DDMMYYXXXX", where `DDMMYY` represents the date of birth, and `XXXX` is a serial number.

## Dependencies

- Python 3.x
- PyMuPDF (`fitz`): This library is used for reading PDF files. It can be installed via pip with `pip install PyMuPDF`.

## Setup

Before running the script, ensure the following variables are correctly set:

- `directory_to_scan`: The path to the directory containing PDF files to be scanned.
- `log_file_path`: The path where the log file, containing found CPR numbers, will be created or appended to.

## Functions

### find_cpr_numbers(text)

- **Purpose**: Scans a given text for CPR numbers matching the expected format.
- **Input**: A string (`text`) to be scanned.
- **Output**: A list of tuples, each containing parts of a found CPR number.

### process_pdf_with_fitz(file_path)

- **Purpose**: Opens a PDF file, reads its text content, and searches for CPR numbers.
- **Input**: The file path to a PDF document.
- **Output**: A list of found CPR numbers in the document. Returns an empty list if no numbers are found or if the file cannot be opened.

### scan_directory_and_log(directory, log_path)

- **Purpose**: Scans all PDF files in the specified directory (and subdirectories), logs found CPR numbers to a specified log file.
- **Input**: 
  - `directory`: Path to the directory to scan.
  - `log_path`: Path to the log file.
- **Behavior**: This function walks through the given directory, processes each PDF file, and logs any found CPR numbers with a timestamp.

## How to Run

1. Ensure all dependencies are installed.
2. Update the `directory_to_scan` and `log_file_path` with appropriate paths.
3. Execute the script in a Python environment.

## Error Handling

- The script includes error handling for empty PDF files, indicated by catching the `fitz.EmptyFileError`. This ensures the script continues even if some files cannot be processed.

## Additional Notes

- The script appends found CPR numbers to the log file, with each execution timestamped to distinguish between different runs.
- Only PDF files are processed. Files with other extensions are ignored.
- The script prints its progress and results to the console, providing immediate feedback on its operation.
