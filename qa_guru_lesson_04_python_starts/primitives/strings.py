
# Учимся писать строки!

s = "i am 'teapot'!"
s = 'i am \'teapot\'!' # "\"-Экранирование
s = """i ""am"" 'teapot'!"""
s = '''i """am""" 'teapot'!'''

multiline_string = """first 
second
third"""

multiline_string = "first\nsecond\nthird" #\n разделение строк
print(multiline_string)

s = "first" + "second"

# Сырые строки
print(r"this is stri\ng") # this is stri\ng  //r - сырая строка, для вывода \n в строке без разделения

# Индексы и слайсы

alphabet = "abcdefg"
alphabet[3] # 'd'
alphabet[2:5] # 'cde'
alphabet[0:5:2] # 'ace'
alphabet[::-1] # 'gfedcba'


# Оперируем - # разобрать дома !!!!



# Форматируем

first = "first"
second = "second"
third = "third"
n = 100

print(f"{first} {second} {third.title()} {n}") # first second Third 100
print("{third} {1} {0}".format(first, second, third=third.title())) # Third second first
print("%s %s %s" % (first, second, third.title())) # first second Third

# Строку в число, и наоборот

str(52132) # '52132'
int("1241241") # 1241241

print("first second third".split()) # ['first', 'second', 'third']
