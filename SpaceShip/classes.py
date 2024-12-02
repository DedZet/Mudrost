from random import randint
from termcolor import cprint, colored
from const import check

class Human:
    def __init__(self):
        self.chars = {"Наука": randint(1, 4), "Инженерия": randint(1, 4), "Лидерство": randint(1, 4)}
    name = 'Имя'
    main_char = 'Специальность'
    char_attack = randint(1, 9)
    char_defence = randint(1, 9)
    char_hp = randint(1, 9)
    def update_config(self):
        if self.main_char == "Учёный": self.chars["Наука"] += 4
        elif self.main_char == "Инженер": self.chars["Инженерия"] += 4
        elif self.main_char == "Лидер": self.chars["Лидерство"] += 4
    def info(self, isplayer):
        if isplayer: print(f"- Имя: {self.name}\n- Наука: {self.chars.get('Наука')}\n- Инженерия: {self.chars.get('Инженерия')}\n- Лидерство: {self.chars.get('Лидерство')}\n")
        else: print(f"- {self.name}\n- Наука: {self.chars.get('Наука')}\n- Инженерия: {self.chars.get('Инженерия')}\n- Лидерство: {self.chars.get('Лидерство')}\n")

class Enemy:
    hp = randint(4,9)
    defence = randint(1,4)
    attack = randint(4,9)
    def hit(self,player_attack):
        if randint(0,11) <= 5: self.hp -= player_attack
        else: self.hp = self.hp + self.defence - player_attack

class Game:
    modes = ["Begin", "Attack","Gameover"]
    mode = "Registration"
    def change_mode(self,m):
        if m == self.modes[0]:
            choices = ["Исследовать ближайшую местность","Построить базу","Отправить дрон на разведку"]
            choice = input("Вы приземлились на Планету-"+str(randint(300, 400))+". Что делать дальше?\n>",'light_green')
            for i in range(len(choices)):
                cprint(str(i+1)+". "+choices[i],'light_green')
                check(choice,choices,self.change_mode)
                ## TODO тут закончел


    
class Map:
    planet_name = "Earth"

    def __init__(self): pass
