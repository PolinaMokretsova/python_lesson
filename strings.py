#строки

m = "my name is Polina" #внутри можно использовать одинарные ковычки
m = 'my name is Polina' #внутри можно использовать двойные ковычки
m = """my name is Polina""" #можно использовать любые ковычки
m = '''my name is Polina''' #можно использовать любые ковычки

multiline_string = """first
                  second
                  third"""

print(multiline_string)

#индексы и слайсы

m = "my name is Polina"
print(m[1]) #в питоне индексация начинается с нуля, поэтому первая буква- нулевая

print(type(m)) #type функция показывающая тип строки


print(m[0:3]) #0:3 диапазон, с какого по какой символ показать

print(m[0:-1]) #диапазон, показывающий все символы кроме последнего

print(m[0:-1:2]) #:2 берет каждый второй символ строки диапазона 0:-1

print(m[0:0:-1]) #:-1 последняя ревертнет порядок символов в другую сторону

#операции над строками

print("Hello, world".replace("Hello", "Hi")) #replace заменяет слово в предложении
print("Hello, world".split()) #split рзделяет предложения на отдельные слова

assert "Hello,world".startswith("Hello") #проверка, что строка начинается на слово хеллоу


print("hello, world".capitalize()) #делает большим первый символ

print("Hello, world".upper()) #делает все буквы большими

#форматирование

first = "firsty"
second = "second"
third = "third"
print(first, second, third)


print(f"{first} {second} {third.title()} {100}")


s = "100"
print(100 + int(s))








