import json
import os
def load_books():
    if os.path.exists('books.json'):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Ошибка при чтении файла books.json: {e}")
            return []
    else:
        return []
def save_books(books):
    try:
        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump(books, file, ensure_ascii=False, indent=4)
        print("Данные успешно сохранены в books.json")
    except IOError as e:
        print(f"Ошибка при сохранении в файл books.json: {e}")
def main():
    books = load_books()
    while True:
        print("\n" + "="*60)
        print("       МЕНЕДЖЕР КНИГ")
        print("="*60)
        print("1. Показать все книги")
        print("2. Добавить книгу")
        print("3. Удалить книгу")
        print("4. Найти книгу")
        print("5. Сохранить изменения")
        print("0. Выход")
        print("-"*60)

        choice = input("Выберите действие (0–5): ").strip()

        if choice == '1':
            pass
            # показать все книги
        elif choice == '2':
            pass
            # добавить книгу
        elif choice == '3':
            pass
            # удалить книгу
        elif choice == '4':
            pass
            # найти книгу
        elif choice == '5':
            save_books(books)
        elif choice == '0':
            print("\nВыход из программы. До свидания!")
            break
if __name__ == "__main__":
    main()