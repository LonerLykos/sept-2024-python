# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'

def extract_numbers(text):
    nums = list()
    x = text.split(' ')
    for i in x:
        y = list(i)
        util_str = ''
        for item in y:
            if item.isdigit():
                util_str += item
        if util_str!= '':
            z = int(util_str)
            nums.append(z)
    print(nums)

extract_numbers(st)