# File Organizer

A simple Python-based file organizer that automatically sorts files into different folders based on their file extensions. The program supports images, PDFs, text files, music, videos, documents, code files, and places unsupported file types into an "Others" folder. It also creates a `log.txt` file in the same directory as the Python program to record every file movement along with the date and time. This project uses Python's built-in `os`, `shutil`, and `datetime` modules and requires no external libraries.

## Features

- Automatically creates category folders
- Organizes files based on file extensions
- Supports Images, PDFs, Text Files, Music, Videos, Documents, and Code
- Places unknown file types in the `Others` folder
- Maintains a log of all file movements
- Records date and time in the log
- Handles permission errors
- Uses UTF-8 encoding for logging

## Requirements

- Python 3.x
- pytest
- pytest-cov

## Usage

Run the program using:

```bash
python main.py
