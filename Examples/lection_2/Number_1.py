# # Создаем список 
# colors = ['red','green','blue123']
# # # создаем переменную 
# data = open('file.txt', 'a')
# data.writelines(colors)
# # data.write('LINE 11221\n')
# # data.write('LINE 11331\n')
# # data.close()


#или записываем по другому

# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

hw_set=[1,3,8,9,10,15,16,16,'my_string','your_string']
hw_set_copy = hw_set.copy()
print(hw_set_copy)
for el in range(len(hw_set)): 
    if el!= int(el):
        hw_set.remove(el)
print(hw_set)
