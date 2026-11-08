# 📝 FastTask — Modern FastAPI & SQLite Task Manager

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org)
[![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

A clean, responsive, and lightweight web-based Task & Todo Management application built using **FastAPI**, **SQLAlchemy ORM**, **SQLite**, and **Jinja2 templates**. Designed with multi-list organization and instant task toggling.

---

## ⚡ Highlights & Key Features

- 📋 **Multi-List Organization**: Group tasks into custom project lists (e.g., Work, Personal, Groceries, Roadmap).
- ✅ **One-Click Task Toggling**: Mark tasks complete or pending with status persistence.
- 🗑️ **Cascade Deletion**: Cleanly delete lists along with all associated tasks using SQLAlchemy cascade relations.
- 🚀 **High Performance Backend**: Powered by FastAPI and asynchronous Uvicorn server for sub-millisecond response times.
- 💾 **Zero-Config Database**: Embedded SQLite database with SQLAlchemy ORM models—runs out of the box with zero setup.
- 🎨 **Responsive UI**: Intuitive web frontend rendered server-side using Jinja2 templates and custom styling.

---

## 🏗️ Architecture & Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) | RESTful routing, dependency injection, and form parsing |
| **ORM & DB** | [SQLAlchemy](https://www.sqlalchemy.org/) + SQLite | Relational schema modeling and local persistence |
| **Templating** | [Jinja2](https://jinja.palletsprojects.com/) | Server-side HTML rendering |
| **ASGI Server** | [Uvicorn](https://www.uvicorn.org/) | Fast lightning ASGI web server |

---

## 📂 Project Structure

```text
to-do-task-manager/
├── database.py       # SQLite connection engine & SessionLocal factory
├── main.py           # FastAPI app, endpoint routing & server initialization
├── models.py         # SQLAlchemy models (TodoList, Task)
├── requirements.txt  # Python package dependencies
├── static/           # Static CSS stylesheets and icons
└── templates/        # Jinja2 HTML templates
    ├── index.html    # Dashboard displaying all lists & quick-add
    └── list.html     # Dedicated single-list view for managing tasks
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.10 or higher
- `pip` package manager

### 1. Clone Repository
```bash
git clone https://github.com/AnupamKhurana/to-do-task-manager.git
cd to-do-task-manager
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install fastapi uvicorn sqlalchemy jinja2 python-multipart
```

### 4. Run the Application
```bash
python3 main.py
```
Or with Uvicorn directly:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open your browser and navigate to: **`http://localhost:8000`**

---

## 🎯 API & Web Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Home dashboard showing all todo lists |
| `POST` | `/add_list` | Create a new todo list container |
| `GET` | `/list/{list_id}` | View and manage tasks inside a specific list |
| `POST` | `/add_task` | Add a new task to an existing list |
| `POST` | `/toggle_task/{task_id}` | Toggle a task's completed state |
| `POST` | `/delete_task/{task_id}` | Remove a task permanently |
| `POST` | `/delete_list/{list_id}` | Remove a list and cascade-delete its tasks |

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
