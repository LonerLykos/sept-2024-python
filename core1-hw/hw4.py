# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

def square_odd_numbers(start, end):
   result = []
   for num in range(start, end + 1):
      if num % 2 != 0:
         result.append(num ** 2)
   return result


print(square_odd_numbers(0, 50))
