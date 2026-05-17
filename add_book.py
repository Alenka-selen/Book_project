import os
import json

def add_book():
    if os.path.exists('books.json'):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла books.json: {e}")
            books = []
    else:
        books = []

    print("\n--- Добавление новой книги ---")
    author = input("Введите автора: ").strip()
    while not author:
        author = input("Введите автора: ").strip()
    title = input("Введите название книги: ").strip()
    while not title:
        title = input("Введите название книги: ").strip()
    score=input("Введите оценку книги: ").strip()
    while not score:
        score = input("Введите оценку книги: ").strip()
    date=input("Введите дату прочтения книги: ").strip()
    while not date:
        date = input("Введите дату прочтения книги: ").strip()
    book={'author': author, 'title': title, 'score': score, 'date': date}
    books.append(book)
    try:
        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при сохранении в файл books.json: {e}")
