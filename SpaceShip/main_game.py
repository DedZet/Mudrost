
from const import *
from classes import *

################# REGISTRATION #################

clear_text()
player.name = input(colored("Введите своё имя\n> ",'yellow'))
clear_text()

select_char()
clear_text()

cprint("Ваши характеристики:",'yellow')
player.update_config()
player.info(True)

cprint('Ваша команда:','yellow')
doctor.info(False)
soldat.info(False)
techno.info(False)
game.change_mode("Begin")