def run ():
    pass
my_list=[1,"Hello", 4.5]
my_dic={"firstname": "Santiago", "lastname": "Mazo"}
super_list=[
    {"firstname": "Santiago", "lastname": "Mazo"},
    {"firstname": "Valeria", "lastname": "Montoya"},
    {"firstname": "Angela", "lastname": "Gaviria"}

]
super_dict={
    "natural_nums":[1,2,3,4,5],
    "integer_nums": [-1,-2,0,1,2],
    "floating_nums": [1.1,4.5,6.43]
    }
for key, value in super_dict.items():
    print(key,"-",value)
if __name__ == '__main__':
    run()