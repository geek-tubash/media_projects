# Django Media Upload Site

This is a Django project that allows users to upload, manage, and delete media files such as images, videos, and audio files.

## Features
- Upload media files (images, videos, audios)
- View uploaded files in a list
- Edit file metadata (e.g. title, tags)
- Delete media files

## Requirements
- Python 3.x
- Django 4.x
- SQLite (or any other database)
- `pip install -r requirements.txt` to install dependencies

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/geek-tubash/5th-contact-assignment.git
    ```
2. Navigate to the project directory:
    ```bash
    cd multimedia_site
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # macOS/Linux
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```

6. Run the server:
    ```bash
    python manage.py runserver
    ```

7. Open your browser and go to:
    ```
    http://127.0.0.1:8000/
    ```

## Usage
- To upload a file, navigate to the "Upload" page.
- Manage files (edit, delete, etc.) from the media list.

## License
MIT License
