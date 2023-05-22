# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]


for i in range(len(students)):
    counter = {}
    name = students[i]['first_name']
    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1

[print(*i, sep=': ') for i in counter.items()]


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# # Самое частое имя среди учеников: Маша
# students = [
#     {'first_name': 'Вася'},
#     {'first_name': 'Петя'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Маша'},
#     {'first_name': 'Оля'},
# ]

for i in range(len(students)):
    counter = {}
    name = students[i]['first_name']
    if name not in counter:
        counter[name] = 1
    else:
        counter[name] += 1

max_name = max(counter, key=counter.get)
print(f"Самое частое имя среди учеников: {max_name}")


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


for groups in school_students:

    counter = {}
    counter_class = 1

    for i in range(len(groups)):
        name = groups[i]['first_name']
        if name not in counter:
            counter[name] = 1
        else:
            counter[name] += 1

    max_name = max(counter, key=counter.get)
    print(f'Самое частое имя в классе {counter_class}: {max_name}')
    counter_class += 1
    counter = {}


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


for i in range(len(school)):
    girls, boys = 0, 0
    group = school[i]['students']
    for k in range(len(group)):
        name = group[k]['first_name']
        if is_male[name]:
            boys += 1
        else:
            girls += 1
    print(f"Класс {school[i]['class']}: девочки {girls}, мальчики {boys}")
    girls, boys = 0, 0


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

school_gender = {}

for i in range(len(school)):
    girls, boys = 0, 0
    group = school[i]['students']
    for k in range(len(group)):
        name = group[k]['first_name']
        if is_male[name]:
            boys += 1
        else:
            girls += 1
    school_gender[school[i]['class']] = {'girls': girls, 'boys': boys}

    girls, boys = 0, 0


for class_name, genders in school_gender.items():
    max_boys = 0
    max_girls = 0
    for key, amount in genders.items():
        if key == 'boys' and amount > max_boys:
            max_boys = amount
            res_boys = {class_name: amount}
        elif key == 'girls' and amount > max_girls:
            max_girls = amount
            res_girls = {class_name: amount}


print(f"Больше всего мальчиков в классе {list(res_boys.keys())[0]}")
print(f"Больше всего девочек в классе {list(res_girls.keys())[0]}")

