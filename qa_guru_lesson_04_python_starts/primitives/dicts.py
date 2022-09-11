
# Заводим словарики
a = 123
d = {
    "key": "value",
    123: a,
    10: {"another": "first"},
    (1, 2, 3): "fafafa"
}

print(d[(1, 2, 3)]) # fafafa

print(d["key"]) # value

# Функции словарей

print(list(d.keys())) # ['key', 123, 10, (1, 2, 3)]
print(list(d.values())) # ['value', 123, {'another': 'first'}, 'fafafa']
print(list(d.items())) # [('key', 'value'), (123, 123), (10, {'another': 'first'}), ((1, 2, 3), 'fafafa')]

print(d.get("browser", "chrome")) # chrome
