import json
import os

def delete():
    if os.path.exists('books.json'):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла books.json: {e}")
            return
    else:
        return
    if not books:
        print('Книг нет.')
        return
    print("\n--- Удаление книги ---")
    author=input('Введите автора книги: ')
    title = input('Введите название книги: ')
    status=False
    for i in books:
        if i['author']==author and i['title']==title:
            status=True
    if not status:
        print('Такой книги в вашем списке нет.')
        return
    for book in range(len(books)):
        if books[book]['author']==author and books[book]['title']==title:
            del books[book]
            break
    print('Книга успешно удалена!')
    save_books(books)

