from csv import reader, writer

with open('products.csv', encoding='utf-8') as data_file:
    csv_data = reader(data_file, delimiter=';')
    result = 0

    for row in csv_data:
        if row[0] == 'Category':
            row[6] += 'total'
        elif row[0] != 'Яйца':
            row[6] += int(row[3]) * int(row[4])
        else:
            row[6] += int(row[4]) * int(row[5])
