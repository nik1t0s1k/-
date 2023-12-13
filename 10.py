import csv

file_name = 'employees.csv'

with open(file_name, encoding='utf-8') as file:
    reader = csv.reader(file)

    next(reader, None)

    employee_data = list(reader)

    '''
    Имя - 0
    Должность - 1 
    Зарплата - 2
    '''
    sorted_employee_data = sorted(employee_data, key=lambda x: int(x[2]))

    with open(file_name, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        fieldnames = ['Имя','Должность','Зарплата']
        writer.writerow(fieldnames)
        writer.writerows(sorted_employee_data)

