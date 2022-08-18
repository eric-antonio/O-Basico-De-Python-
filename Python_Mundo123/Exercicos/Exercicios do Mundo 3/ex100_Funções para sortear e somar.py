from random import randint
from time import sleep


def sortear(lista):
    for i in range(0, 4):
        n =randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.2)


def somaPar(li):
    soma = 0
    for i in li:
        if i % 2 == 0:
            li.append(i)

    print(li)

numeros = list()
sortear(numeros)
somaPar(numeros)
