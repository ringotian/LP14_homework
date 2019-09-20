"""
Домашнее задание №2
Дата и время
* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    """
    print(f'Today is {datetime.now().strftime("%d/%m/%Y")}')
    print(f'Yesterday was {datetime.strftime(datetime.now()-timedelta(days=1), "%d/%m/%Y")}')
    print(f'Previous month date was {datetime.strftime(datetime.now()+relativedelta(months = -1), "%d/%m/%Y")}')



    
    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    """
    return datetime.strptime(string, '%m/%d/%y %H:%M:%S.%f')
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime('01/01/17 12:10:03.234567'))
