
phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book


def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding ='UTF-8' ) as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))

