

def main_menu():
    commands = ['Показать все контакты', 
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт', 
                'Найти контакт', 
                'Выйти из программы']
    print('Выберите пункт меню: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('Введите пункт меню: '))
    while 1 > user_input > 8:
        print('Такого пункта в меню нет.') 
        user_input = int(input('Выберете пункт с 1 по 8 : '))
    return user_input

def show_contacts(phone_book: list):
    if len(phone_book)>0:
        for item in phone_book:
            print(item)
    else:
        print('Телефонная книга пуста или не загружена')
