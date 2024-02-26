from csv import reader

with open('products.csv', encoding='utf-8') as data_file:
    csv_data = reader(data_file, delimiter=';')
    for row in csv_data:
        name = ''
        while name != 'молоко':
            name = input()
            if name == 'молоко':
                break
            else:
                product = ''
                count = 0
                if name in row[0]:
                    if not 'Яйца' in row[0]:
                        count1 = count
                        count = min(int(row[4]), count)
                        if count1 != count:
                            product = row[1]
                    else:
                        count1 = count
                        count = min(int(row[5]), count)
                        if count1 != count:
                            product = row[1]
                if product == '':
                    print('Такой категории не существует в нашей БД')
                else:
                    print(f'В категории: {name} товар {product} был куплен {count} раз')