from random import randint
from time import sleep

print('\033[0;33m *' * 20)
print('\033[0;32m  Vamos Jogar Par/Impar?')
print('\033[0;33m *' * 20)
resultado = 0
condicao = 1
contV = contajogos = 0

while True:
    if condicao <= 0:
        break

    jogador = int(input('\033[0;33m Isira um valor: \033[m'))
    res = ' '
    while res not in 'PI':
        res = str(input('\033[0;33m Insira Impara ou Par?[I/P]: \033[m ')).upper().strip()[0]

    pc = randint(0, 11)
    resultado = jogador + pc

    if res == 'I':
        if resultado % 2 == 1:
            print(f'\033[0;32m Você Jogou: {jogador} e escolheu : {res}'
                  f'. O seu adversario (PC) Jogou: {pc} \n'
                  f'A soma disso deu:{resultado} ', end='')
            print('Par...' if resultado % 2 == 0 else 'Impar...')
            print('\033[0;34m Então você Ganhou!\033[m ')
            contV += 1
        else:
            print(f'\033[0;32m Você Jogou: {jogador} e escolheu : {res}'
                  f'. O seu adversario (PC) Jogou: {pc} .\n'
                  f'A soma disso deu:{resultado} ', end='')
            print('Par...' if resultado % 2 == 0 else 'Impar...')
            print(f'\033[0;31m  Então você perdeu! \033[m ')
            condicao = 0


    elif res == 'P':
        if resultado % 2 == 0:
            print(f'\033[0;32m Você Jogou: {jogador} e escolheu : {res}'
                  f'. O seu adversario (PC) Jogou: {pc} .\n'
                  f'A soma disso deu:{resultado} ', end='')
            print('Par...' if resultado % 2 == 0 else 'Impar...')
            print('\033[0;34m Então você Ganhou!. \033[m ')
            contV += 1
        else:
            print(f'\033[0;32m Você Jogou: {jogador} e escolheu : {res}'
                  f'. O seu adversario (PC) Jogou: {pc} .\n'
                  f'A soma disso deu:{resultado} ', end='')
            print('Par...' if resultado % 2 == 0 else 'Impar...')
            print(f'\033[0;31m  Então você perdeu! \033[m ')

            condicao = 0

    contajogos += 1


print(f'Em um total de {contajogos} jogos você ganhou {contV} vezes!')
print('Acbou!....')
