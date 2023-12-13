import csv

employees_data = [
    {'Имя': 'Алексей', 'Должность': 'Програмист', 'Зарплата': 400},
    {'Имя': 'Дмитрий', 'Должность': 'Системный администратор', 'Зарплата': 3000},
    {'Имя': 'Иван', 'Должность': 'Маркетолог', 'Зарплата': 1000},
    {'Имя': 'хзкто', 'Должность': 'Граф дизайнер', 'Зарплата': 10000}
]

file_name = 'employees.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    file_names = ['Имя', 'Должность', 'Зарплата']
    writer = csv.DictWriter(file, file_names)

    writer.writeheader()

    for employee in employees_data:
        writer.writerow(employee)
print(f'Данные успешно записаны в файл:{file_name}')
