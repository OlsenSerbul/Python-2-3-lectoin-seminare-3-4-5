# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

f = open('new_file.txt', 'r' )
data = f.read()+''
f.close
count = 0
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

print(rle_code(data))

#не пойму как избавится от 1  в конце "слова" !?

def rle_decode(data):
    decode = '' 
    count = ''
    for char in data:
        if char.isdigit(): 
             count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

print(rle_decode(data))




