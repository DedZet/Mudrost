# p = input("Введите число ")

# num = int(p[0:-2])

# if len(p) >= 3:
#     if p[-2] == 'h' and p[-1] == 'm': print(num*60)
#     if p[-2] == 'h' and p[-1] == 's': print(num*60*60)

#     if p[-2] == 'm' and p[-1] == 'h': print(num/60)
#     if p[-2] == 'm' and p[-1] == 's': print(num*60)

#     if p[-2] == 's' and p[-1] == 'm': print(num/60)
#     if p[-2] == 's' and p[-1] == 'h': print(num/60*60)

#     if p[-2] == p[-1]: print(num, 'Одинаковые аргументы')
#     else: "Недостаточно аргументов"

#2####################################################

# def calculate_profit(deposit, y):
#     if deposit < 30000:
#         print("Минимальный вклад составляет 30 000 рублей")
#     profit = 0

#     if y <= 3: 
#         rate = 0.03
#         profit_add = min((deposit // 10000) * 0.003, 0.05) + rate
#     elif y >= 4 and y < 6: 
#         rate = 0.05
#         profit_add = min((deposit // 10000) * 0.003, 0.05) + rate + 0.03 
#     elif y > 6: 
#         rate = 0.02
#         profit_add = min((deposit // 10000) * 0.003, 0.05) + rate + 0.03 + 0.05

#     profit = (deposit * ((1 + profit_add) ** y)) - deposit

#     return round(profit, 2)

# deposit_amount = float(input("Введите сумму вклада: "))
# investment_years = int(input("Введите срок вклада: "))
# print(calculate_profit(deposit_amount, investment_years))

#3#################################################

# u = input('Введите диапазон ')
# nums_inp = u.split()
# num1 = int(nums_inp[0])
# num2 = int(nums_inp[1])
# s = []

# print(num1, num2)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# for x in range(num1, num2 - 1):
#     if is_prime(x): s.append(x)

# if len(s) != 0: print(s)
# else: print('Error!')

#4#################################################
# i = j = 0
# inp_scale = int(input("Введите размер матрицы: "))
# print('')
# class MatrixA:
#     scale = 2
#     slot = [][:scale]
#     rows = [][:scale]

# class MatrixB:
#     scale = 2
#     slot = [][:scale]
#     rows = [][:scale]
    
# a = c = MatrixA()
# b = MatrixB()

# while i < inp_scale:
#     inp_slot_a = (input(f"Введите {i+1}-ю строку матрицы A: ")).split()[:inp_scale]
#     inp_slot_a = list(map(lambda x: int(x), inp_slot_a))
#     a.rows.append(inp_slot_a)
#     i += 1
# print('')
# while j < inp_scale:
#     inp_slot_b = (input(f"Введите {i+1}-ю строку матрицы B: ")).split()[:inp_scale]
#     inp_slot_b = list(map(lambda x: int(x), inp_slot_b))
#     b.rows.append(inp_slot_b)
#     j += 1

# print('')
# print("Matrix A:",a.rows)
# print("Matrix B:",b.rows)
# print('')

# for i in range(len(a.rows)):
#     for j in range(len(b.rows)):
#      c.rows[i][j] = a.rows[i][j] + b.rows[i][j]

# print("Matrix C:", c.rows)

#5#################################################

# str_inp = input("Введите строку: ")
# def palindrome(x):
    
#     u = ''.join(x.split()).lower()

#     if u[0:len(x)] == u[::-1]:
#         print('Да')
#     else: print('Нет')

# palindrome(str_inp)