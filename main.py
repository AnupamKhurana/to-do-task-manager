from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import TodoList, Task
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    lists = db.query(TodoList).all()
    return templates.TemplateResponse("index.html", {"request": request, "lists": lists})

@app.post("/add_list")
def add_list(title: str = Form(...), db: Session = Depends(get_db)):
    todo_list = TodoList(title=title)
    db.add(todo_list)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/add_task")
def add_task(list_id: int = Form(...), title: str = Form(...), db: Session = Depends(get_db)):
    task = Task(title=title, list_id=list_id)
    db.add(task)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/toggle_task/{task_id}")
def toggle_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = not task.completed
        db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete_task/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/delete_list/{list_id}")
def delete_list(list_id: int, db: Session = Depends(get_db)):
    todo_list = db.query(TodoList).filter(TodoList.id == list_id).first()
    if todo_list:
        db.delete(todo_list)
        db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/list/{list_id}", response_class=HTMLResponse)
def view_list(request: Request, list_id: int, db: Session = Depends(get_db)):
    todo_list = db.query(TodoList).filter(TodoList.id == list_id).first()
    if not todo_list:
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("list.html", {"request": request, "list": todo_list})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)