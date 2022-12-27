# 2'. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])

# list = [2, 3, 5, 6]
# result = []
# for i in range(len(list) // 2 + len(list) % 2):
#     result.append(list[i] * list[-(i + 1)])
# print(result)

list = [int(x) for x in input().split()]
print([x * y for x, y in zip(list[:len(list) // 2 + len(list) % 2], list[::-1])])
