import json
import os

def show():
    if os.path.exists('books.json'):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла books.json: {e}")
            books = []
    else:
        books = []
    if not books:
        print('Книг нет.')
        return
    print("\n" + "="*60)
    print('Список книг: ')
    for book in books:
        print('-'*40)
        print(f'Книга номер {book["id"]}')
        print(f'Автор: {book["author"]}')
        print(f'Название: {book["title"]}')
        print(f'Оценка: {book["score"]}')
        print(f'Дата прочтения: {book["date"]}')
        print('-' * 40)
        print()
    print("=" * 60)
def middle_score():
    if os.path.exists('books.json'):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла books.json: {e}")
            books = []
    else:
        books = []
    if not books:
        print('Книг нет.')
        return
    summa=0
    number=0
    for book in books:
        number+=1
        summa+=book['score']
    print(f'Средняя оценка всех книг: {round(summa/number, 2)}')
def stats():
    if os.path.exists('books.json'):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла books.json: {e}")
            books = []
    else:
        books = []
    if not books:
        print('Книг нет.')
        return
    authors={}
    for book in books:
        if book['author'] not in authors:
            authors[book['author']]=1
        else:
            authors[book['author']]+=1
    print("\n" + "=" * 60)
    print('Статистика авторов: ')
    for author in authors:
        print(f'{author}: {authors[author]}')
    print("=" * 60)