# 1)Дан list:
list1 = [22, 3,5,2,8,2,-23, 8,23,5]

#   - знайти мін число
min_num = min(list1)
print(min_num)

#   - видалити усі дублікати
list2 = list(set(list1))
print(list2)

#   - замінити кожне 4-те значення на 'X'
def replace_fourth(lst):
    for i in range(3, len(lst), 4):
        lst[i] = 'X'
    return lst

print(replace_fourth(list1))
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def print_square(side:int):

    if side == 0:
        print('Invalid input. Side length must be a positive integer.')
        return
    j = side
    while j > 0:
        if (j == 1) or (j == side):
            print('*' * side)
        else:
            print('*' +' ' * (side - 2) + '*')
        j -= 1

print_square(5)


# 3) вивести табличку множення за допомогою цикла while

def multi_table():
    i = 2
    while i<=9:
        j = 1
        while j<=10:
            print(f'{i} * {j} = {i*j}', end='\n')
            j += 1
        i += 1

multi_table()

# 4) переробити це завдання під меню
list = [22, 3,5,2,8,2,-23, 8,23,5]
while True:
    a = int(input('працюємо з наступним списком [22, 3,5,2,8,2,-23, 8,23,5]\n'
                  'введіть число від 1 до 6 для обрання вашого варіанту\n'
                  '1. Знайти мінімальне число\n'
                  '2. Видалити дублікати\n'
                  '3. Замінити кожне 4-те значення на "X"\n'
                  '4. Вивести пустий квадрат з "*" сторону якого вкажіть самостійно після обрання поточного варіанту\n'
                  '5. Вивести табличку множення\n'
                  '6. Вихід\n'))
    if a == 1:
        print(min(list))
    elif a == 2:
        print(set(list))
    elif a == 3:
        replace_fourth(list)
    elif a == 4:
        b = (input('введіть сторону квадрата: '))
        if not b.isdigit():
            print('Невірно введений вхідний параметр.\n')
            continue
        elif int(b):
            print_square(int(b))
    elif a == 5:
        multi_table()
    elif a == 6:
        break

