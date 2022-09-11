# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__

def my_func_for_print_func_and_arg(function, *args):
    function = function.__name__.replace('_', ' ').capitalize()     # с помощью replace(), заменяем "_" на пробел. capitalize() - первая буква в верхний регистр, остальные в нижний
    print(function, *args)

def open_browser(browser_name):
    my_func_for_print_func_and_arg(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    my_func_for_print_func_and_arg(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    my_func_for_print_func_and_arg(find_registration_button_on_login_page, page_url, button_text)

open_browser('Chrome или Firefox')
go_to_companyname_homepage('https://qa.guru/python')
find_registration_button_on_login_page('https://qa.guru/python', "\"Знак войти\"(XPath'[href=\"https://qa.guru/cms/system/login\"]')")
