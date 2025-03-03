
# - створити функцію яка виводить ліст

def print_list(lst):
    print(lst)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def find_max(a: int | float, b: int | float, c: int | float):
    print(max(a, b, c))


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def find_max_min(*args: int | float)-> int | float:
    print(max(*args))
    return min(*args)


# - створити функцію яка повертає найбільше число з ліста

def find_max_in_list(lst: list):
    util_lst = []
    for i in lst:
        if type(i) is int:
            util_lst.append(i)
    if not util_lst:
        return "No numbers in the list"
    else: return max(util_lst)


# - створити функцію яка повертає найменьше число з ліста

def find_min_in_list(lst: list):
    util_lst = []
    for i in lst:
        if type(i) is int:
            util_lst.append(i)
    if not util_lst:
        return "No numbers in the list"
    else:
        return min(util_lst)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_of_list(lst: list[int | float]):
    return sum(lst)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def average_of_list(lst: list[int | float]):
    return sum(lst) / len(lst)
