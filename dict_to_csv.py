"""
Домашнее задание №2
Работа csv
* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv
"""
import csv

def main():
    csv_content = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]
    fields = []
    for i in csv_content:
        fields = list(i.keys())
    with open("people.csv","w",encoding='utf8',newline = '') as f:
        writer = csv.DictWriter(f, fields, delimiter = ';')
        writer.writeheader()
        for i in csv_content:
            writer.writerow(i)

if __name__ == "__main__":
    main()