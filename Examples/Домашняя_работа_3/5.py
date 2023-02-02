# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k= int(input('Сколько раз будем складывать? '))

poz_fib = [0,1]
neg_fib = [0,1]
index = 0
index1=0
while len(poz_fib) <= k:
    poz_fib.append(poz_fib[index]+ poz_fib[index+1])
    index += 1

while len(neg_fib) <= k:
    neg_fib.append(- neg_fib[index1+1] + neg_fib[index1] )

    index1 += 1

neg_fib.reverse()
print(f'Результат:  {neg_fib[:-1] + poz_fib}')
