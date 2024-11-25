# tasks = [("Проверить почту", 3), 
#          ("Написать отчёт", 1), 
#          ("Позвонить клиенту", 2)]

# a = sorted(tasks, key=lambda x: x[0])

# print(a)

##########################################################
# purchases = [
#     {"item": "Laptop", "price": 1000, "quantity": 2},   
#     {"item": "Mouse", "price": 25, "quantity": 5},    
#     {"item": "Keyboard", "price": 45, "quantity": 3}
# ]

# lam_func = list(map(lambda x: x.get("price")*x.get("quantity") ,purchases ))
# print(max(lam_func))
##########################################################
# clients = [
#     {"name": "Alice", "income": 50000},    
#     {"name": "Bob", "income": 120000},    
#     {"name": "Charlie", "income": 70000}
# ]
# for x in range(len(clients)):
#     if clients[x].get("income") > 100000: clients[x]["category"]="high"    
#     elif 50000 < clients[x].get("income") < 100000: clients[x]["category"]="medium"    
#     else: clients[x]["category"]="low"
#     s = dict(clients)
#     lam_func = list(map(lambda x: {**x, "category":"high"} if x.get("income") > 100000 else {**x, "category":"medium"} if 50000 < x.get("income") < 100000 else {**x, "category":"low"}, clients ))
# print(lam_func)
##########################################################
# flights = [
#     {"flight": "A1", "departure": 9, "arrival": 12},    
#     {"flight": "B2", "departure": 14, "arrival": 18},    
#     {"flight": "C3", "departure": 6, "arrival": 8}
# ]

# lam_func = list(filter(lambda x: x.get("arrival") < 12,flights ))
# print(lam_func)
##########################################################
messages = [
    {"user": "Исследователь А", "message": "Отчёт готов. Ссылка: http://foundation.org"},
    {"user": "Доктор Б", "message": "Документы можно найти здесь: https://classified.com"},
    {"user": "Охранник В", "message": "Нет аномальной активности за смену."},
    {"user": "Агент Г", "message": "Срочно изучите материалы по объекту 173 на http://statue-database.net"},
    {"user": "Д-р Кляйн", "message": "Обновлённый протокол эксперимента доступен: https://safezone.scp"},
    {"user": "Сотрудник Д", "message": "Просьба ознакомиться с https://docs.anomalies-secure.com перед сменой."},
    {"user": "Старший учёный Л", "message": "Все записи переданы. Никаких аномалий на объекте 096."},
    {"user": "Техник З", "message": "Проблема с сервером устранена. Подробнее: http://fix-report.internal"}
]

import re

url = re.compile(r'https?://\S+')
redacted = list(filter(lambda y: "http" in y.get("message"),messages))
lam_func = list(map(lambda x: x.update({"message":url.sub('[ДАННЫЕ УДОЛЕНЫ]', x.get("message"))}), redacted))

print(redacted)