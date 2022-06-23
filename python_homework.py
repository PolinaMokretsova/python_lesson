# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и ее аргументов.
# Вызовите ее для трех функций ниже в цикле
# Подсказка: Имя функции можно получить с помощью func.__name__

def open_browser():
    pass


def go_to_companyname_homepage():
    pass


def find_registration_button_on_login_page():
    pass

i = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for g in i:
    string_name = g.__name__
    print(string_name)