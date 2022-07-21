from random import  randint
from  time import  sleep
lista = list()
jogos = list()
print(f'\033[0;33m-=-\033[m'*15)
print(f'\033[0;34m Seja bem vindo a Super Loto'.center(50, ' '))
print(f'\033[0;33m-=-\033[m'*15)
quant = int(input(f'Quantos jogos deseja Sortear?: '))
tot = 1
while tot <= quant:
    con = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            con += 1

        if con >= 6:
            break
    lista.sort()
    jogos.append([lista[:]])
    lista.clear()
    tot +=1
print(f'\033[0;35m-=\033[m'*3, f'\033[0;32m Sorteando {quant} Jogos!', '\033[0;35m-=\033[m'*3)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'\033[0;33m Boa Sorte!'.center(40, ' '))