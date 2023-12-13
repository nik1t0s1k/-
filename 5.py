import csv

file_name = 'employees.csv'


name = input('Введите имя работника: ')
post = input('Введите должность работника: ')
salary = input('Введите зарплата работника: ')

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow([name, post, salary])

print(f'работник: {name} успешно добавлено в файл: {file_name}')

