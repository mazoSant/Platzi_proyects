def run ():
    my_dict={}
    for i in range(1,101):
        if i%3==0:
            continue
        my_dict[i]=i**3
    print(my_dict)
run()
#Aca en la segunda manera se hace de una manera mejor
def run ():
    my_dict={i:i**3 for i in range (1,101) if i%3 !=0}

    print(my_dict)
run()
#A continuación agregare un diccionario con las raices cuadradas de los mil primeros numeros
import math as math
def run ():
    my_dict={i:math.sqrt(i) for i in range (1,101) if i%3 !=0}

    print(my_dict)
run()