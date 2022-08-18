from random import randint
from time import sleep


def sortear(lista):
    print(f'Sorteando 5 Valores')
    for i in range(0, 4):
        n =randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.2)
    print()


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = list()
sortear(numeros)
somaPar(numeros)
