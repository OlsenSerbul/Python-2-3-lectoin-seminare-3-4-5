# Создаем список 
colors = ['red','green','blue']
# создаем переменную 
data = open('file.txt', 'a')
data.writelines(colors)
data.close()