def run():
    numeros=[]
    for i in range (1,101):
        if i%3 !=0:
            continue
        numeros.append(i**2)
    print(numeros)


if __name__ == '__main__':
    run()
