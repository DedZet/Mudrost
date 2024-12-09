import os
from termcolor import cprint, colored

SPECIALS = ["Рыдцарь", "Лучник", "Гоблин"]
MODES = ["Search", "Attack"]

MAPS = ["в Оружейной","в Библиотеке","во Дворце", "в Сокровищнице", "в Столовой"]
CHOICES = ["Штурм","Инвентарь","Характеристики (Пропуск)"]

clear_text = lambda: os.system('cls')

################# FUNCTIONS #################
def println(s,arr,color):
    print(str(s))
    for i in range(len(arr)):
        cprint(str(i+1)+". "+arr[i],color)

def choice(choices,retry_str):
    println(retry_str,choices,'yellow')
    s = input('> ')
    try: 
        if int(s) > len(choices) or int(s) < 1:
            clear_text()
            cprint("Несуществующий выбор\n",'red')
            return choice(choices,retry_str)
        else: return int(s)
    except ValueError:
        clear_text()
        cprint("Вы ввели не число\n",'red')
        return choice(choices,retry_str)



