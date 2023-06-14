import csv


with open('msc_bus.csv', encoding='utf-8') as file:
    headers = csv.DictReader(file, delimiter=';')
    for header in headers:
        fields = header.values()
        break

    src = csv.DictReader(file, delimiter=';', fieldnames=fields)
    lst = []
    for string in src:
        street = string['Описание места расположения объекта']
        if street:
            try:
                comma = street.index(',')
                lst.append(street[:comma])
            except ValueError:
                lst.append(street)
    print('Количество остановок:', len(lst))
    print('Улица, на которой больше всего остановок:', max(lst, key=lst.count))
