#s = '1 2 3 4 5 6 7 8 9 0'.split()
# for i in range(len(s)):
#    if s[i] == '3':
#        s[i] = '30'
#        print(s)
################################## 
#s = '1 2 3 4 5'.split()
#for i in range(len(s)):
#     s[i] = int(s[i])**2
#print(s)
################################## 
#s = [1,2,3,4,56,76,4,3,11,13,23]
#print(max(s) / len(s))
##################################
# s = (1,2,34,54,7,3,1,3,5,76)
# print(sorted(s))
##################################
# shop = {'apple':5,'pie':3,'berry':12,'avocado':7}

# min_item = 100
# max_item = 1

# for i in shop:
#     if shop.get(i) >= max_item:
#         max_item = shop.get(i)
#     elif shop.get(i) <= min_item: min_item = shop.get(i)
# print(min_item, max_item)
##################################
# s = 'aa bb cc ds ef tr'.split()
# d = {}

# for i in s:
#     d[i] = i
# print(d)
##################################
# words = {'apple':'яблоко','bone':'кость'}
# p = input('Введит ерусское слово ')

# print( list(words.keys())[list(words.values()).index(p)] )
##################################
from random import randint

con_str = "\n1. Камень\n2. Ножницы\n3. Бумага\n4. Ящерица\n5. Спок\n"

obj = int(input("Ваш ход: "))
if obj not in [1,2,3,4,5]:
    print("Неверный ход")
    exit()
    
comp = randint(1,5)

game_lose = (obj == 1 and (comp == 3 or comp == 5)) or (obj == 2 and (comp == 1 or comp == 5)) or (obj == 3 and (comp == 2 or comp == 4)) or (obj == 4 and (comp == 2 or comp == 1)) or (obj == 5 and (comp == 4 or comp == 3))
game_win = (obj == 3 and (comp == 1 or comp == 5)) or (obj == 1 and (comp == 2 or comp == 4)) or (obj == 2 and (comp == 3 or comp == 4)) or (obj == 4 and (comp == 5 or comp == 3)) or (obj == 5 and (comp == 1 or comp == 2)) 
def game():
    if game_lose:
        print("Поражение")
    elif game_win:
        print("Победа")
    else: print("Ничья")
    
game()
