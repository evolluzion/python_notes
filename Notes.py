# Начинаем наш проект по созданию приложения для заметок
import json
from datetime import datetime

# Файл для хранения заметок
FILE_NAME = 'notes.json'

# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(FILE_NAME, 'w') as f:
        json.dump(notes, f, indent=4, default=str)

# Функция для создания новой заметки
def create_note():
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": input("Введите заголовок заметки: "),
        "body": input("Введите тело заметки: "),
        "date": datetime.now()
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка создана.")

# Функция для отображения списка заметок
def list_notes(filter_date=None):
    notes = load_notes()
    for note in notes:
        if filter_date is None or note['date'].startswith(filter_date):
            print(f"{note['id']}: {note['title']} ({note['date']})")

# Функция для чтения заметки
def read_note():
    notes = load_notes()
    id_to_read = int(input("Введите ID заметки: "))
    note = next((note for note in notes if note["id"] == id_to_read), None)
    if note:
        print(f"Заголовок: {note['title']}\nТело: {note['body']}\nДата: {note['date']}")
    else:
        print("Заметка не найдена.")

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    id_to_edit = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == id_to_edit:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новое тело заметки: ")
            note['date'] = datetime.now()
            save_notes(notes)
            print("Заметка обновлена.")
            break
    else:
        print("Заметка не найдена.")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    id_to_delete = int(input("Введите ID заметки для удаления: "))
    notes = [note for note in notes if note["id"] != id_to_delete]
    save_notes(notes)
    print("Заметка удалена.")

# Главное меню приложения
def menu():
    while True:
        print("\nКонсольное приложение для работы с заметками")
        print("1. Создать заметку")
        print("2. Список всех заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            filter_date = input("Введите дату для фильтрации в формате YYYY-MM-DD или нажмите Enter для показа всех заметок: ")
            list_notes(filter_date)
        elif choice == '3':
            read_note()
        elif choice == '4':
            edit_note()
        elif choice == '5':
            delete_note()
        elif choice == '6':
            break
        else:
            print("Неверная команда. Попробуйте снова.")

# Запуск приложения
if __name__ == "__main__":
    menu()