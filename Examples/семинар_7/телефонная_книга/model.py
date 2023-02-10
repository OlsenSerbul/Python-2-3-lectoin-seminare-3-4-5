
tel_book = {'мама': 45678,'муж': 2344566, 'сын': 34567899, 'папа': 4556789, 'брат': 3456777}




# 1 - показать все
def show_all(tel_book):
    for item in tel_book.items():
        print(item)
# 2 - найти контакт
def find_contact(value_number, tel_book):
    
    for key, value in tel_book.items():
        if key == str(value_number):
           return value
        elif value == int(value_number):
           return key
        else:
            return 'такого контакта нет'

# 3 - добавить контакт
def add_name(value_number, tel_book):
    for key, value in tel_book.keys():
        if key == value_number:
            return f'данный контакт уже есть {key, value}'
        else:
            tel_book[value_number] = 0
def add_number(vallue_number, tel_book):
    for key,value in tel_book.values():
        if value == int(vallue_number):
           return f'Такой контакт уже есть {key, value}'
        else:
            tel_book[key] = vallue_number
            return tel_book

# 4 - удалить контакт
def del_cont(value_number, tel_book):
    for key,value in tel_book:
        if key == value_number or value == int(value_number):
            tel_book.pop(key,value)
            return tel_book
        else:
            return 'такого контакта нет'
# 5 - изменить контакт
def change_cont(new_value_number, value_number, tel_book):
    for key, value in tel_book:
        if key == value_number:
            tel_book[key] = tel_book[new_value_number]
            return tel_book
        elif value == int(value_number):
            value = int(new_value_number)
            return tel_book

# 6- выход
def exit():
    print('телефонная книга закрыта')





   






