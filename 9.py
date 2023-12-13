import csv as biba

new_file_name = input('Введите  имя нового файла: ')

with open(new_file_name, 'w', newline='', encoding='utf-8') as file:
    employee_data = [
        {
            'Имя': 'Алексей',
            'Должность': 'Разработчик игр',
            'Зарплата': '3500'
        },
        {
            'Имя': 'Дминтрий',
            'Должность': 'Мобильный разработчик',
            'Зарплата': '2050'
        }
    ]
    writer = biba.writer(file)
    for item in employee_data:
        writer.writerow([item['Имя'], item['Должность'], item['Зарплата']])

with open(new_file_name, 'r', newline='', encoding='utf-8') as file:
    reader = biba.reader(file)
    for item in reader:
        print(item[0], '-', item[1])

