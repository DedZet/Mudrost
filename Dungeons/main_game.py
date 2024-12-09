
from const import choice, println, clear_text, SPECIALS, MODES, CHOICES, MAPS
from classes import *
from random import seed

player = Player()


def select_char():
    player.main_char = SPECIALS[choice(SPECIALS,"Выберите класс: ")-1]

def inventory():
    clear_text()
    if len(player.inventory) == 0: cprint("Инвентарь пуст\n",'grey')

chudak = Enemy()
obstacle = ''
current_map = MAPS[0]
def search():
    global chudak
    chudak = Enemy()
    global obstacle
    global current_map
    current_map = MAPS[randint(0,4)]
    print(f"Вы находитесь {current_map}")
    if randint(0,10) <= 5: obstacle = "Никого нет"
    else: obstacle = chudak.name

def search_item(map):
    if map == "в Оружейной": return "Ничего"
    elif map == "В Библиотеке": return "Зелье"
    elif map == "в Столовой": return "Яблоко"
    elif map == "во Дворце" or map == "в Сокровищнице":
        player.score += 20
        cprint(f"Вы нашли сокровища", "light_blue")
        return "Ничего"

def mode(m):
    while player.char_hp > 0:
        if m == MODES[0]: #Search
            search()
            made_choice = choice(CHOICES,f"Перед вами {obstacle}")
            clear_text()
            if made_choice == 1 and obstacle != "Никого нет": # Действие + Враг
                return mode("Attack")

            elif made_choice == 1 and obstacle == "Никого нет": # Действие + Нет врага
                if randint(0,10) <= 5: player.give_item(search_item(current_map))
                return mode("Search")

            elif made_choice == 2 and (obstacle != "Никого нет" or obstacle == "Никого нет"): # Инвентарь
                inventory()
                if player.inventory != []:
                    use_item = choice(player.inventory,"Ваш инвентарь: ")
                    if player.inventory[use_item-1] == "Зелье":
                        cprint(f"Вы выпили зелье, ваша сила увеличилась.\n","light_blue")
                        player.char_attack += 2
                    elif player.inventory[use_item-1] == "Яблоко":
                        cprint(f"Вы съели яблоко, ваше здоровье увеличилось.\n","light_blue")
                        player.char_hp += 2
                    elif player.inventory[use_item-1] == "Подозрительное зелье":
                        if randint(0,10) <= 5: 
                            player.char_hp += 6
                            cprint(f"Вы выпили подозрительное зелье, ваше здоровье увеличилось.\n","light_blue")
                        else: 
                            player.char_hp -= 4
                            cprint(f"Вы выпили подозрительное зелье, ваше здоровье ухудшилось.\n","red")
                    del player.inventory[use_item-1]
                    mode("Search")
            elif made_choice == 3 and (obstacle != "Никого нет" or obstacle == "Никого нет"): # Характеристики
                    player.info()
        if m == MODES[1]: #Attack
            cprint(f"Вы ударили {obstacle}\n{obstacle} ударил вас!", "red")
            chudak.hit(player.char_attack)
            cprint(f"Ваше здоровье: {player.char_hp}\n", "red")
            player.hit(chudak.attack)
            if chudak.hp <= 0:
                player.give_item(chudak.drop)
                player.score += 5
                mode("Search")

################# REGISTRATION #################


clear_text()
player.name = input("Введите своё имя\n> ")
clear_text()

select_char()
clear_text()
player.update_config()
del select_char
del SPECIALS

player.info()
mode("Search")


