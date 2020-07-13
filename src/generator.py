import csv
import json
import os

books = os.path.abspath('../data/books.csv')
books_list = os.path.abspath('../data/books_list.json')
users_and_books = os.path.abspath('../data/users_and_books_result.json')
users = os.path.abspath('../data/users.json')

# Открываем файл с книгами чтобы сохранить каждую строку в список, чтобы потом дальше перевести в json
with open(books) as file_with_books:
    book_list = []
    csv_reader = csv.DictReader(file_with_books)
    for row in csv_reader:
        book_list.append(row)


# Конвертируем в словарь json
with open(books_list, 'w') as books_json:
    json.dump(book_list, books_json, sort_keys=True, indent=4)

'''Открываем файлы с книгами и пользователями, итерируемся, чтобы в контекстном менеджере в итоге преобразовать в 
единый файл '''
with open(books_list) as books_list_json:
    json_data_books = json.load(books_list_json)
    for book in json_data_books:
        with open(users, 'r') as user_json:
            users_json_data = json.load(user_json)
            output_result = []
            for item in users_json_data:
                output_result.append(
                    {'name': item["name"], 'gender': item["gender"], 'address': item["address"], 'books': book})
    with open(users_and_books, 'w') as users_books_result:
        json.dump(output_result, users_books_result, sort_keys=True, indent=4)
