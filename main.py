import json

#функция для открытия телефонной книги
def open_phonebook():
    try:
        with open("phonebook.json", "r") as file:
            phonebook = json.load(file)
        return phonebook
    except FileNotFoundError:
        return {}

#функция для сохранения телефонной книги
def save_phonebook(phonebook):
    with open("phonebook.json", "w") as file:
        json.dump(phonebook, file)

#функция для показа контактов
def show_contacts(phonebook):
    for contact in phonebook:
        print(f"Имя: {contact}, Номер: {phonebook[contact]}")

#функция для создания контакта
def create_contact(phonebook):
    name = input("Введите имя контакта: ")
    number = input("Введите номер телефона: ")
    phonebook[name] = number
    print("Контакт создан")

#функция для поиска контакта
def find_contact(phonebook):
    name = input("Введите имя контакта для поиска: ")
    if name in phonebook:
        print(f"Имя: {name}, Номер: {phonebook[name]}")
    else:
        print("Контакт не найден")

#функция для изменения контакта
def edit_contact(phonebook):
    name = input("Введите имя контакта для изменения: ")
    if name in phonebook:
        new_number = input("Введите новый номер телефона: ")
        phonebook[name] = new_number
        print("Контакт изменен")
    else:
        print("Контакт не найден")

#функция для удаления контакта
def delete_contact(phonebook):
    name = input("Введите имя контакта для удаления: ")
    if name in phonebook:
        del phonebook[name]
        print("Контакт удален")
    else:
        print("Контакт не найден")

#Главное меню
def main_menu():
    print("\nГлавное меню")
    print("1. Открыть телефонную книгу")
    print("2. Сохранить телефонную книгу")
    print("3. Показать контакты")
    print("4. Создать контакт")
    print("5. Найти контакт")
    print("6. Изменить контакт")
    print("7. Удалить контакт")
    print("8. Выход")

phonebook = {}
while True:
    main_menu()
    choice = input("Выберите пункт меню: ")
    if choice == "1":
        phonebook = open_phonebook()
    elif choice == "2":
        save_phonebook(phonebook)
    elif choice == "3":
        show_contacts(phonebook)
    elif choice == "4":
        create_contact(phonebook)
    elif choice == "5":
        find_contact(phonebook)
    elif choice == "6":
        edit_contact(phonebook)
    elif choice == "7":
        delete_contact(phonebook)
    elif choice == "8":
        print("Выход из программы")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите снова.")