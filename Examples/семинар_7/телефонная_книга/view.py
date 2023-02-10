def show_menu():
    print('Добро пожаловать!Выберите действие:\n1 - показать весь телефонный стравочник\n'
          '2 - найти контакт\n3 - добавить контакт\n4 - удалить контакт\n5 - изменить контакт\n'
          '6 - выход')
def get_value():
    return int(input('Введите номер действия : '))

def get_value_number():
    value_number = (input('Введите значение : '))
    return value_number

def get_new_value_number():
    new_value_number = (input('Введите новое значение : '))
    return new_value_number
    
def print_console():
    print()