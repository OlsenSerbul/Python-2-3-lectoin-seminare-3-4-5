import model

def input_class():
    return input('С каким классом работаем?  ').upper()

def input_subject():
    subject = input('Введите первую букву названия предмета:  ').lower()
    if subject == 'р':
        print('Открыт предмет: русский язык')
        return 'русский язык'
    if subject == 'л':
        print('Открыт предмет: литература')
        return 'литература'
    if subject == 'а':
        print('Открыт предмет: алгебра')
        return 'алгебра'
    if subject == 'г':
        print('Открыт предмет: геометрия')
        return 'геометрия'
    if subject == 'ф':
        print('Открыт предмет: физика')
        return 'физика'
    if subject == 'х':
        print('Открыт предмет: химия')
        return 'химия'
    if subject == 'б':
        print('Открыт предмет: биология')
        return 'биология'
    else:
        return 'Предмет не найден или введена цифра'

def who_answer(journal: dict):
    who_answer = input('Кто будет отвечать?  ')
    for child in journal:
        if who_answer == journal.get(child):
            return child
    else:
       return 'Ученик не найден.'

def what_marc():
    return input('На какую оценку ответил?  ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')
