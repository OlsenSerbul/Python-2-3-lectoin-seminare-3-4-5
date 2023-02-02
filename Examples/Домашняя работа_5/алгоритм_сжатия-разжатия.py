# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

f = open('new_file.txt', 'r' )
data = f.read() + ''
f.close()


print(data)
def rle_code(data): 
    encoding = '' 
    povt_char = '' 
    count = 1 
    if not data: 
       return ''
    for char in data: 
        if char != povt_char:
            if povt_char: 
                encoding += str(count) + povt_char 
            count = 1 
            povt_char = char 
        else: 
            count += 1 
    else: 
        encoding += str(count) + povt_char 
        return encoding
code = rle_code(data)
print(code)
print()
#не пойму как избавится от 1  в конце "слова" !?

def rle_decode(data):
    decoding = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else :
            if not count:
                decoding += char
            else: 
                decoding += int(count) * char
                count = ''
    return decoding
decode = rle_decode(data)
print(decode)






