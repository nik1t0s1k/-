import csv

file_name = 'employees.csv'

with open(file_name, newline='', encoding='utf-8') as file:

    reader = csv.reader(file)

    next(reader, None)

    employee_data = list(reader)

    for item in reversed(employee_data):
        print(item[0], '-', item[1])

print('Вывели студентов в обратном порядке')

