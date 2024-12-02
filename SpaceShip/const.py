import os
from classes import *

SPECIALS = ["Учёный", "Инженер", "Лидер"]
clear_text = lambda: os.system('cls')

################# CHARACTERS #################

player = Human()

doctor = Human()
doctor.name = "Доктор Гастрит (Учёный)"
doctor.main_char = "Учёный"
doctor.update_config()

soldat = Human()
soldat.name = "Сержант Блейк (Солдат)"
soldat.main_char = "Лидер"
soldat.update_config()

techno = Human()
techno.name = "Паша Техник (Инженер)"
techno.main_char = "Инженер"
techno.update_config()

game = Game()

################# FUNCTIONS #################
def select_char():
    num = (input(colored("Введите специализацию:\n1. Учёный \n2. Инженер\n3. Лидер\n> ",'yellow')))
    check(num,SPECIALS,select_char())
    player.main_char = SPECIALS[int(num)-1]

def check(s,choices,retry_func):
    try: s = int(s)
    except ValueError:
        clear_text()
        cprint("Вы ввели не число",'red')
        return retry_func
    if int(s) > len(choices) or int(s) < 1:
        clear_text()
        cprint("Несуществующий выбор",'red')
        return retry_func
