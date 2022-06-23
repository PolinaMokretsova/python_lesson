def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]


def function_name(func):
    for arg in func:
        print("Имя функции:", arg.__name__, end='. ')
        if not any(arg.__code__.co_varnames):
            print("No arguments")
        else:
            print("Аргумент функции:", arg.__code__.co_varnames)


function_name(functions)
