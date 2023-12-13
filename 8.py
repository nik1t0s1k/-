import csv

file_name = 'employees.csv'

with open(file_name, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    employee_data = list(reader)

    for item in employee_data:
        print(item[0], '-', item[1])

    name_remove = input('Введите имя работника для удаления: ')

    remove_student = [item for item in employee_data if item[0] != name_remove]

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['Имя', 'Должность']
        writer.writerow(fieldnames)
        writer.writerows(remove_student)
    print(f'Работник ({name_remove}) успешно удален из файла: {file_name}')

    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            print(row['Имя'], '-', row['Должность'], )
