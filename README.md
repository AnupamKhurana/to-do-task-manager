# Todo Task Manager

> **App Root Folder:** `/mnt/1fc0b605-b95c-4190-ba0a-ae87f22cc120/development/to-do-task-manager`


A simple todo list web application built with FastAPI, SQLAlchemy, and Jinja2.
purely Using vibe coding (gpt-oss-20b with kilo in vscode)

## Features

- Create, read, update, and delete tasks.
- Mark tasks as completed.
- Simple web interface.

## Setup

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in your browser.

## Project Structure

- `main.py` – FastAPI application.
- `models.py` – SQLAlchemy models.
- `database.py` – Database setup.
- `templates/` – Jinja2 templates.
- `static/` – Static files (CSS).
