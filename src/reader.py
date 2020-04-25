import csv, json
books = list()
#  читаем csv
with open('../data/books.csv', newline='') as f:
    reader = csv.reader(f)

    # Извлекаем заголовок
    header = next(reader)


    # Итерируемся по данным делая из них словари
    for row in reader:
        books = (dict(zip(header, row)))
        print(books)


print('*' * 100)
#  читаем файл json
with open("../data/users.json", "r") as f:
    users = json.loads(f.read())
print(users)
    # for user in users:
    #     dict = user['name'] + user['address'], user['gender']
    #     print(dict)

