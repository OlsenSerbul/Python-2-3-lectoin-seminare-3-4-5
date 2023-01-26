# Работа со списками

# dict_ = {'id': 4, 'person':'human', 'name': 'Rokki', 'age': 38, 'work': 'boks'}
# dict_2 = {'id': 6, 'car': 'priora'}

# # сложить словари:

# dict_.update(dict_2)
# print(dict_)


storage = {'ананас': 4, 'киви': 4, 'банан': 7, 'арбуз': 2, 'дыня': 2 }
delivery = {'ананас': 6, 'арбуз': 2, 'инжир': 7 }

# выведем два словара для сравнения
print(storage)
print(delivery)

# делаем обьединение словарей

# storage.update(delivery)
# print(storage)

# но если нужно сложить значения вложенные в ключи, нужно:

# создаем множество
keys = set()

# добавляем в множество значения из первого словаря
for key in storage:
    keys.add(key)

# # добавляем значения второго словаря в множество keys

for key in delivery:
    keys.add(key)

# делаем сложение значений:

for key in keys:
    storage[key] = storage.get(key, 0) + delivery.get(key, 0)

print(storage)

# функция для покупки товара поштучно

def buy(name: str):
    storage[name] = storage.get(name) -1 

buy('банан')
print(storage)

#  с помощью цикла вывести ключи

for k in storage.keys():
    print(k)

#  с помощью цикла вывести значения:

for k in storage.values():
    print(k)

# вывести значение ключ-значение( кортеж):

for k , v in storage.items():
    print(f'На складе {v} позиций товара "{k}"')