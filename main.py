from csv import reader, writer

with open('products.csv', encoding='utf-8') as data_file:
    csv_data = reader(data_file, delimiter=';')
    result = 0
    for item in csv_data:
        if item[0] == 'Закуски':
            result += float(item[4]) * float(item[3])
    print(result)
