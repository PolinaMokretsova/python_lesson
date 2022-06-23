
# Заводим словарики

d = {
    "key": "value",
    123: "another",
    10: {"another": "first"},
}

print(d["key"])

print(list(d.keys())) #список ключей
print(list(d.values())) #список значений

# Функции словарей

print(list(d.items())) #items связка пар ключ значение

d["first"] = "some string" #присвоили ключу ферст строку

print(d)

value = d.pop("first") #удаление ключа 