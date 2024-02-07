# Начинаем наш проект по созданию приложения для заметок
import json
import random
from datetime import datetime

# Файл для хранения заметок
FILE_NAME = 'notes.json'

# Функция генерации уникального ID для заметок
def generate_unique_id(existing_ids, id_length=4):
    range_start = 10**(id_length - 1)
    range_end = (10**id_length) - 1
    while True:
        unique_id = random.randint(range_start, range_end)
        if unique_id not in existing_ids:
            return unique_id

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
    existing_ids = {note['id'] for note in notes}
    while True:
        title = input("\nВведите название заметки: ")
        body = input("Введите текст заметки: ")
        if title == "" or body == "":
            print("\nОШИБКА: Поля не могут быть пустыми! Повторите попытку!")
            continue
        note_id = generate_unique_id(existing_ids, 5)
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%d.%m.%Y")
        current_time = current_datetime.strftime("%H:%M:%S")
        note = {
            "id": note_id,
            "title": title,
            "body": body,
            "date": current_date,
            "time": current_time
        }
        notes.append(note)
        save_notes(notes)
        print("\nЗаметка создана.")
        input()
        break
    

# Функция для отображения списка заметок
def list_notes(filter_date=None):
    notes = load_notes()
    if not notes:
        print("В файле заметок пока пусто!")
        input()
        return
    filtered_notes = []
    for note in notes:
        if filter_date is None or note['date'].startswith(filter_date):
            filtered_notes.append(note)
    if filtered_notes:
        sorted_notes = sorted(filtered_notes, key=lambda x: (x['date'], x['time']), reverse=True)
        for note in sorted_notes:
            print(f"{note['id']}: {note['title']} ({note['date']} {note['time']})")
    else:
        print("\nИнформация по данному фильтру отсутствует. Проверьте ввод еще раз (ДД.ММ.ГГГГ)!")
    input()

# Функция для чтения заметки
def read_note():
    notes = load_notes()
    while True:
        id_to_read = input("\nВведите ID заметки: ")
        if id_to_read == "":
            print("\nОШИБКА: Поле ввода не может быть пустым!")
            continue
        if not id_to_read.isdigit():
            print("\nОШИБКА: Поле ввода не может содержать буквы или десятичные числа!")
            continue
        id_to_read = int(id_to_read)
        note = next((note for note in notes if note["id"] == id_to_read), None)
        if note:
            print(f"\nНазвание: {note['title']}\nТекст: {note['body']}\nДата: {note['date']} {note['time']}")
            input()
        else:
            print("\nЗаметка не найдена.")
            input()
        break

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    while True:
        id_to_edit = input("\nВведите ID заметки для редактирования: ")
        if id_to_edit == "":
            print("\nОШИБКА: Поле ввода не может быть пустым!")
            continue
        if not id_to_edit.isdigit():
            print("\nОШИБКА: Поле ввода не может содержать буквы или десятичные числа!")
            continue
        id_to_edit = int(id_to_edit)
        for note in notes:
            if note["id"] == id_to_edit:
                new_title = input("\nВведите новое название заметки: ")
                new_body = input("Введите новый текст заметки: ")
                if new_title == "" or new_body == "":
                    print("\nОШИБКА: Поля не могут быть пустыми! Повторите попытку!")
                    continue
                note['title'] = new_title
                note['body'] = new_body
                current_datetime = datetime.now()
                note['date'] = current_datetime.strftime("%d.%m.%Y")
                note['time'] = current_datetime.strftime("%H:%M:%S")
                save_notes(notes)
                print("\nЗаметка обновлена.")
                input()
                break
        else:
            print("\nЗаметка не найдена.")
            input()
        break

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    while True:
        id_to_delete = input("\nВведите ID заметки для удаления: ")
        if id_to_delete == "":
            print("\nОШИБКА: Поле ввода не может быть пустым!")
            continue
        if not id_to_delete.isdigit():
            print("\nОШИБКА: Поле ввода не может содержать буквы или десятичные числа!")
            continue
        id_to_delete = int(id_to_delete)
        note_found = False
        for note in notes:
            if note["id"] == id_to_delete:
                notes.remove(note)
                note_found = True
                break
        if not note_found:
            print("\nОШИБКА: Такого ID не существует!")
            continue
        save_notes(notes)
        print("\nЗаметка удалена.")
        input()
        break

# Главное меню приложения
def menu():
    while True:
        print("  ____    _____    __   __   ______  _______  _    _  _     _ ")
        print(" (____)  (_____)  (__)_(__) (______)(__ _ __)(_)  (_)(_)   (_)")
        print("(_) _(_)(_)___(_)(_) (_) (_)(_)__      (_)   (_)_(_) (_) _(__)")
        print(" _ (__) (_______)(_) (_) (_)(____)     (_)   (____)  (_)(_)(_)")
        print("(_)__(_)(_)   (_)(_)     (_)(_)____    (_)   (_) (_) (__)  (_)")
        print(" (____) (_)   (_)(_)     (_)(______)   (_)   (_)  (_)(_)   (_)")
        print("                       by Napolskiy Boris (GeekBrains Student)")
        print("\nГлавное меню:")
        print("1. Создать заметку")
        print("2. Вывести список всех заметок")
        print("3. Прочитать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выход")
        
        choice = input("\nВыберите действие: ")

        if choice == '1':
            create_note()
        elif choice == '2':
            filter_date = input("Введите дату для фильтрации в формате ДД.ММ.ГГГГ или нажмите Enter для показа всех заметок: ")
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
            print("\nОШИБКА: Неверная команда! Попробуйте снова.")
            input()

# Запуск приложения
if __name__ == "__main__":
    menu()