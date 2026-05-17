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
        print("1. Добавить книгу")
        print("2. Показать список книг")
        print("3. Рассчитать среднюю оценку книг")
        print("4. Вывести статистику авторов")
        print("5. Удалить книгу")
        print("-"*60)

        choice = input("Выберите действие (1–5), enter для выхода: ").strip()
        if not choice:
            print("\nВыход из программы.")
            break
        if choice == '1':
            add_book()
        elif choice == '2':
            show()
        elif choice == '3':
            middle_score()
        elif choice == '4':
            stats()
        elif choice == '5':
            delete()
if __name__ == "__main__":
    main()