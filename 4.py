import csv
with open('employees.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader, None)
    min_salary = 1500
    for index, row in enumerate(reader):
        if index == 0:
            continue
        elif int(row[2]) > min_salary:
            print(f'Сотрудник {row[0]}: {int(row[2])}')
