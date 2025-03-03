# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'

def extract_numbers(st):
    dirtyLi = list(st)
    clearLi = list()
    for i in dirtyLi:
        if i.isdecimal():
            clearLi.append(i)
    return clearLi

print(', '.join(extract_numbers(st)))
