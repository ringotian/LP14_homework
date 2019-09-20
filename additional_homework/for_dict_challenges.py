# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
students_list = []
for dictionary in students:
    students_list.append(dictionary['first_name'])
from collections import Counter
names = Counter(students_list)
for name in names:
    print(f'{name}: {names[name]}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
students_list = []
for dictionary in students:
    students_list.append(dictionary['first_name'])
names = Counter(students_list).most_common(1)
print('Самое частое имя среди учеников: {}'.format(names[0][0]))


# Пример вывода:
# Самое частое имя среди учеников: Маша



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
counter = 0
for school_classes in school_students:
    schoolers = []
    counter = counter + 1
    for school_class in school_classes:
        schoolers.append(school_class['first_name'])
    names = Counter(schoolers).most_common(1)
    print('Самое частое имя в классе {}: {}'.format(counter, names[0][0]))
   
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
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

for school_class in school:
    name_list = []
    for name in school_class['students']:
        name_list.append(name['first_name'])
    girls_counter = 0
    boys_counter = 0
    for name in name_list:
        if name in is_male.keys():
            if not is_male[name]:
                girls_counter = girls_counter + 1
            else:
                boys_counter = boys_counter + 1    
    print("В классе {} {} девочки и {} мальчика".format(school_class['class'], girls_counter, boys_counter))

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
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
class_info = {}
for school_class in school:
    name_list = []
    for name in school_class['students']:
        name_list.append(name['first_name'])
    girls_counter = 0
    boys_counter = 0
    for name in name_list:
        if name in is_male.keys():
            if not is_male[name]:
                girls_counter = girls_counter + 1
            else:
                boys_counter = boys_counter + 1    
    class_info[school_class['class']] = {'girls': girls_counter, 'boys': boys_counter}

girls_max = 0
boys_max = 0
class_max=''
for class_name in class_info:
    if class_info[class_name]['girls'] > girls_max:
        girls_max = class_info[class_name]['girls']
        class_max = class_name
print(f'Больше всего девочек в классе {class_max}')

class_max=''
for class_name in class_info:
    if class_info[class_name]['boys'] > boys_max:
        boys_max = class_info[class_name]['boys']
        class_max = class_name
print(f'Больше всего мальчиков в классе {class_max}')

   
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a