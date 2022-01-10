#Primero veremos la funcion filter
#Aca lo resolvemos con list comprehensions
my_list=[1,4,5,6,9,13,19,21]
odd=[i for i in my_list if i%2 !=0 ]
print(odd)
#Ahora aplicamos la funcion filter
my_list=[1,4,5,6,9,13,19,21]
odd=list(filter(lambda x: x%2 !=0, my_list))
print(odd)


#Ahora veremos la funcion map
#Queremos elevar todos los numeros de mi lista al cuadrado y primero usamos list comprehensions
my_list=[1,4,5,6,9,13]
squares=[i**2 for i in my_list]
print(squares)
#Ahora con map
my_list=[1,4,5,6,9,13]
squares=list(map(lambda x:x**2,my_list))
print(squares)

 

#Ya veremos la funcion reduce
#Tenemos una lista y queremos que se multipliquen los numeros de la lista
my_list=[2,2,2,2,2]
multiplicador=1
for i in my_list:
    multiplicador=multiplicador*i
print(multiplicador)
#Ahora lo haremos con la funcion reduce
from functools import reduce
my_list=[2,2,2,2,2]
producto=reduce(lambda a, b:a*b,my_list)
print(producto)