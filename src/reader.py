import csv, json

from csv import DictReader

books_input = []
with open('../data/books.csv', newline='') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        # print(row)
        books_input = row


print(books_input)
# with open("../data/users.json", 'r') as json_file:
#     users_input = json.loads(json_file.read())
#     print(users_input)





# # запись в файл
# with open("../data/users_output.json", 'w') as j_f:
#     s = json.dumps(a, indent=4)
#     j_f.write(s)


# users_output = []
# keys_sorting = ['name', 'gender', 'address']
#
# for keys_sorting in users_input:
#     users = {}
