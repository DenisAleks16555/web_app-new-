import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com"


def get_books_from_web():
    """
    Функция должна вернуть список книг.
    Пример: [{'title': 'A Light in the Attic', 'price': '£51.77'}, ...]
    """
    print(f"Парсим сайт {URL}...")

    # ==========================================
    # ПРАКТИКА №2: Логика парсинга
    # Мы напишем requests.get и soup.find_all
    # ==========================================

    # 1. Получить страницу
    # 2. Создать суп
    # 3. Найти книги (тег article, класс product_pod)

    return []  # Пока возвращаем пустой список
