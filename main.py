import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

# Импортируем настройки (Book импортируем позже, когда напишем)
from database import SessionLocal, create_db  # , Book
from parser import get_books_from_web

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Создаем таблицы (если они описаны)
create_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================================
# ПРАКТИКА №3: Роуты и Связывание
# ==========================================


@app.get("/")
def home(request: Request):
    # Задача: Достать книги из БД и передать в шаблон
    return templates.TemplateResponse("index.html", {"request": request, "books": []})


@app.get("/load")
def load_books():
    # Задача: Спарсить и сохранить в БД
    return "Здесь будет загрузка книг"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
