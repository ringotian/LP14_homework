"""
Домашнее задание №2
Работа с файлами
* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длину получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf8') as f:
        content = f.read()
        print(f'Str length: {len(content)}\nWords: {len(content.split())}')
    
    with open('referat.txt', 'r', encoding='utf8') as f:
        for line in f:
            with open('referat2.txt','a',encoding='utf8') as f2:
                f2.write(line.replace('.', '!'))





if __name__ == "__main__":
    main()