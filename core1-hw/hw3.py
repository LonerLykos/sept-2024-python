# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

def capitalize_characters(string):
    upper = string.upper()
    return list(upper)

print(capitalize_characters(greeting))