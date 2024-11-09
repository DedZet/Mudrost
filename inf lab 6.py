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

# def calculate_profit(deposit, years):
#     if deposit < 30000:
#         print("Минимальный вклад составляет 30 000 рублей.")

#     if years <= 3:
#         interest_rate = 0.03
#     elif 4 <= years <= 6:
#         interest_rate = 0.05
#     else:
#         interest_rate = 0.02

#     additional_interest = min((deposit // 10000) * 0.003, 0.05)
    
#     total_interest_rate = interest_rate + additional_interest

#     final_amount = deposit * ((1 + total_interest_rate) ** years)

#     profit = final_amount - deposit

#     return round(profit, 2)

# deposit_amount = float(input("Введите сумму вклада (в рублях): "))
# investment_years = int(input("Введите срок вклада (в годах): "))
# profit = calculate_profit(deposit_amount, investment_years)

# print(f"Сумма прибыли составит: {profit} рублей.")

#3#################################################

u = input('Введите число ')

nums = u.split()

num1 = int(nums[0])
num2 = int(nums[1])

print(num1, num2)
def is_prime(p):
    for x in range(num1, num2 - 1): 
        if (p % x == 0): 
            print(x)

is_prime(num1)

#4#################################################

# def input_matrix(size):
#     matrix = []
#     for _ in range(size):        
#         row = list(map(int, input().strip().split()))
#         matrix.append(row)    
#         return matrix

# def add_matrices(matrix1, matrix2):
#     if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):        
#         raise ValueError("Матрицы должны быть одинакового размера!")
#     result = []
#     for i in range(len(matrix1)):        
#         row = []
#         for j in range(len(matrix1[i])):            
#             row.append(matrix1[i][j] + matrix2[i][j])
#         result.append(row)
#     return result

# def main():    
#     size = int(input("Введите размер матриц (N): "))
#     print("Введите элементы первой матрицы:")
#     matrix1 = input_matrix(size)
#     print("Введите элементы второй матрицы:")    
#     matrix2 = input_matrix(size)
#     result_matrix = add_matrices(matrix1, matrix2)
#     print("Результат сложения двух матриц:")
#     for row in result_matrix:        
#         print(' '.join(map(str, row)))

# main()

#5#################################################

