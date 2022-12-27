# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# num=input('Введите число: ')
# sum=0
# for i in num:
#     if i != '.':
#         sum+=int(i)
# print(f'Сумма {num} равна: {sum}')

number = float(input('Введите число: '))
print(sum(map(int, [x for x in str(number) if x.isnumeric()])))
