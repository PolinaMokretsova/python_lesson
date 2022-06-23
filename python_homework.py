# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser(arg1="Открываем браузер"):
    pass



def go_to_companyname_homepage(arg2="Домашняя страница"):
    pass





def find_registration_button_on_login_page(arg3="Находим кнопку регистрации на странице авторизации"):
    pass


import inspect

def function_name(*args):
    for function in args:
       arguments = inspect.signature(function)
       print( "Имя функции:", function.__name__, "Ее понятное имя-аргумент", arguments)

function_name(open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)

