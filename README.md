# Todo Task Manager

A simple todo list web application built with FastAPI, SQLAlchemy, and Jinja2.

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