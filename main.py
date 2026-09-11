import shutil
import os
from datetime import datetime


CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "PDFs": [".pdf"],
    "TextFiles": [".txt", ".md", ".csv"],
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".docx", ".xlsx", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".json"],
    "Others": []
}


def get_cat_path():
    path1 = input("Enter path to folder: ")

    if not os.path.exists(path1):
        print("Path does not exist!")
        return None

    if not os.path.isdir(path1):
        print("This is not a folder!")
        return None

    return path1


def create_folders(path1):
    for category in CATEGORIES:
        os.makedirs(
            os.path.join(path1, category),
            exist_ok=True
        )


def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()

    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category

    return "Others"


def log_move(filename, category):
    # Directory where this Python file exists
    code_directory = os.path.dirname(os.path.abspath(__file__))

    log_path = os.path.join(code_directory, "log.txt")

    curr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"[{curr}] {filename} → {category}/\n")


def organize(path1):
    files = [
        f for f in os.listdir(path1)
        if os.path.isfile(os.path.join(path1, f))
    ]

    if not files:
        print("No files to organize!")
        return

    for filename in files:
        category = get_category(filename)

        source = os.path.join(path1, filename)
        destination = os.path.join(path1, category, filename)

        try:
            shutil.move(source, destination)

            log_move(filename, category)

            print(f"Moved: {filename} → {category}/")

        except PermissionError:
            print(f"Permission denied: {filename} — skipping")


def main():
    path1 = get_cat_path()

    if path1 is None:
        return

    create_folders(path1)
    organize(path1)


if __name__ == "__main__":
    main()