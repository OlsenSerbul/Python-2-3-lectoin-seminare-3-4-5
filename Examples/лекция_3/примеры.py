#1/ lambda
# Создаем классическую функцию 
def sum(x, y):
    return x+y

def mult(x, y):
    return x*y

# создаем новую функцию, к которую определяем уже имеющуюся функуцию в качестве аргумента

def calc(op, a, b):
    print(op(a,b))
#   return op(a, b)

calc(mult, 34, 43)
# избавляемся от классического описания
# def sum(x, y):
#     return x+y
# заменяем на:
f = lambda x,y: x+y

calc(f, 5, 9)
# упрощаем запись до:
calc(lambda x, y: x+y)