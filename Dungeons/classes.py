from random import randint
from termcolor import cprint, colored

class Player:
    def __init__(self):
        self.chars = ["Рыдцарь","Лучник","Гоблин"]
    name = 'Имя'
    main_char = 'Класс'

    char_attack = randint(3, 9)
    char_defence = randint(3, 9)
    char_hp = randint(3, 9)
    score = 0

    inventory = []
    def update_config(self):
        if self.main_char == "Рыдцарь": self.char_hp += 5
        elif self.main_char == "Лучник": self.char_attack += 5
        elif self.main_char == "Гоблин": self.char_defence += 5
    def info(self):
        print("Ваши характеристики:")
        cprint(f"- Имя: {self.name}\n- Защита: {self.char_defence}\n- Атака: {self.char_attack}\n- Здоровье: {self.char_hp}\n- Сокровища: {self.score}\n","light_green")
    def give_item(self, item):
        cprint(f"Вы получили: {item}","light_green")
        if item != "Ничего":
            self.inventory.append(item)
    def hit(self,enemy_attack):
        if self.char_defence > 0: self.char_defence -= enemy_attack
        else: 
            self.char_hp -= enemy_attack
            self.char_defence = 0
        if self.char_hp <= 0:
            cprint(f"Вы умерли", "red")
        

class Enemy:
    enemys = ["Ведьма", "Кабан", "Шаман", "Зонбе"]
    drop = name = ''

    hp = randint(1,4)
    defence = randint(1,4)
    attack = randint(1,4)

    def __init__(self):
        
        self.name = self.enemys[randint(0,3)]
        if self.name == self.enemys[0]:
            self.drop = "Зелье"
            self.hp += 5
        elif self.name == self.enemys[1]:
            self.drop = "Яблоко"
            self.defence += 3
            self.attack += 3
        elif self.name == self.enemys[2]:
            self.drop = "Подозрительное зелье"
            self.hp += 6
            self.attack += 4
        elif self.name == self.enemys[3]:
            self.drop = "Ничего"


    def hit(self,player_attack):
        self.hp -= player_attack
        if self.hp <= 0:
            cprint(f"Вы убили {self.name}", "light_green")

player = Player()

