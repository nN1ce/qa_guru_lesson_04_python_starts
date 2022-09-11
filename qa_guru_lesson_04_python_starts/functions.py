
# Объявляем функции и аргументы

def func():      # фунуция
    print("I'm called")

func() # I'm called (вызов функции )
func() # I'm called
# exit(0) - завершенние кода до этого момента
def print_message(message, end):
    print(message, end=end)


print_message("hello", end=", ")
print_message(message="world", end=".")
print()  # hello, world.

# exit(0)
# Возвращаем значение

def lower_string(string: str):
    return string.lower()

def upper_and_lower_string(string: str):
    return string.upper(), string.lower()


print(lower_string("CAPITALIZED WORDS")) # capitalized words
print(lower_string("HelO WoOoOrlD!")) # helo woooorld!

print(upper_and_lower_string("HelO WoOoOrlD!")) # ('HELO WOOOORLD!', 'helo woooorld!')


# Переменное количество аргументов


def print_all_arguments(*args):
    print(*args) # 1 2 3 4 5 6 7 8, если print(args) => (1, 2, 3, 4, 5, 6, 7, 8)


print_all_arguments(1, 2, 3, 4, 5, 6, 7, 8)

# exit(0)
def func_with_kwargs(**kwargs):
    print(kwargs)


func_with_kwargs(key=123, second=321)


def wrapped_print(*args, **kwargs):
    print("Начинаем печать")
    print(*args, **kwargs)
    print("Заканчиваем печать")


wrapped_print('Печатаем', end="\n\n")

def print_all_arguments(end, *args):
    for arg in args:
        print(arg, end=end)


print_all_arguments("", 2, 3, 4, 5, 6, 7, 8)


def print_all_arguments(*args, end="\n"):
    for arg in args:
        print(arg, end=end)


def print_all_arguments_v2(*args, end="\n"):
    print(*args, end=end)


print_all_arguments(2, 3, 4, 5, 6, 7, 8, end="")
print()
print_all_arguments_v2(2, 3, 4, 5, 6, 7, 8, end="\n")


# Переменное количество возвращаемых значений

def f():
    return 1, 2, 3

# Функция - тоже объект

def by_age(d):
    return d["age"]

by_age({"name": "Oleg", "age": 32})

users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]

print(sorted(users, key=by_age)) # [{'name': 'Stanislav', 'age': 15}, {'name': 'Maria', 'age': 18}, {'name': 'Sergey', 'age': 24}, {'name': 'Oleg', 'age': 32}, {'name': 'Olga', 'age': 45}]
print(max(users, key=by_age)) # {'name': 'Olga', 'age': 45}
print(min(users, key=by_age)) # {'name': 'Stanislav', 'age': 15}