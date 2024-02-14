import os
import re
import fitz  # PyMuPDF, ensure it's installed via pip install PyMuPDF
from datetime import datetime

# Directory to scan
directory_to_scan = '/...'  # Update this path accordingly
# Log file path
log_file_path = '/.../cpr_numbers_log.txt'  # Ensure this path is correct

def find_cpr_numbers(text):
    # Matches CPR numbers in the format "DDMMYY-XXXX" or "DDMMYYXXXX"
    pattern = r'\b(0[1-9]|[12]\d|3[01])(0[1-9]|1[012])(\d{2})(-?)(\d{4})\b'
    return re.findall(pattern, text)

def process_pdf_with_fitz(file_path):
    try:
        doc = fitz.open(file_path)
        text = ''
        for page in doc:
            text += page.get_text()
        doc.close()
        return find_cpr_numbers(text)
    except fitz.EmptyFileError:  # Catching the specific error
        print(f"Cannot open or the file is empty: {file_path}")
        return []  # Return an empty list indicating no CPR numbers found

def scan_directory_and_log(directory, log_path):
    print(f"Starting to scan directory: {directory}")
    log_entries = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                full_path = os.path.join(root, file)
                print(f"Processing PDF file: {full_path}")
                found_cpr_numbers = process_pdf_with_fitz(full_path)
                if found_cpr_numbers:
                    for num in found_cpr_numbers:
                        # Format each CPR number with a hyphen for uniformity
                        formatted_number = f"{num[0]}{num[1]}{num[2]}-{num[4]}"
                        log_entry = f"{os.path.basename(full_path)}: {formatted_number}"
                        log_entries.append(log_entry)
                        print(f"Found CPR number: {formatted_number}")
                else:
                    print("No CPR numbers found in this file.")

    if log_entries:
        with open(log_path, 'a') as log_file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_file.write(f"Log timestamp: {timestamp}\n")
            for entry in log_entries:
                log_file.write(entry + "\n")
        print("CPR numbers logged successfully.")
    else:
        print("No CPR numbers found or all files skipped due to errors.")

if __name__ == "__main__":
    scan_directory_and_log(directory_to_scan, log_file_path)
