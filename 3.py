import csv

file_name = 'employees.csv'

new_employees = [
    {
        'Имя': 'Вадим',
        'Должность': 'Аналитик',
        'Зарплата': 1700
    },
    {
        'Имя': 'Яков',
        'Должность': 'Админ баз данных',
        'Зарплата': 2000
    },
]

with open(file_name, 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    for employee in new_employees:
        writer.writerow([employee['Имя'], employee['Должность'], employee['Зарплата']])
print(f'Данные успешно записаны в файл:{file_name}')