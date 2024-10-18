from termcolor import cprint

for x in range(-10,11):
    for y in range(-10,11):
        for x2 in range(-10,11):
            for y2 in range(-10,11):
                print(f'A [{x};{y}] B [{x2};{y2}]')
                cprint(f'     C [{x+x2};{y+y2}]', 'yellow')
                cprint('--------------------','black')