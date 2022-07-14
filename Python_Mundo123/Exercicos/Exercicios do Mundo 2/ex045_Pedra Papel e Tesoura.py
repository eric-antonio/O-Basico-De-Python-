from  random import  randint
from time import sleep
list = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint (0,2)

print(''' \033[0;33m Escolha uma das opcoes:
    0- Pedra
    1- Papel
    2- Tesoura''')
jogador = int(input('\033[0;35m Insira a sua jogada: '))

print('\033[1;34m Jo!' , end= '')
sleep(1)
print('\033[1;35m ken!', end= '')
sleep(1)
print('\033[1;36m Po!')
sleep(1)
 

print('\033[0;32m Voce  escolheu\033[m \033[0;34m- {}'.format(list[jogador]))
print('\033[0;32m O computador escolheu\033[m \033[0;34m- {}'.format(list [computador]))
if computador ==0:
    if jogador ==0:
        print('Emapate!')
    elif jogador ==1:
        print('Jodador Ganhou!')
    elif jogador ==2:
        print('Computador Venceu!')
    else:
        print('\033[0;31m Jogada Invalida!')

elif computador ==1:
    if jogador ==0:
        print('Computador Venceu!')
    elif jogador ==1:
        print('Emapate!')

    elif jogador ==2:
        print('Jodador Ganhou!')
    else:
        print('\033[0;31m Jogada Invalida!')

elif computador ==2:

    if jogador ==0:
        print('Jodador Ganhou!')
    elif jogador ==1:
        print('Computador Venceu!')
    elif jogador ==2:
        print('Emapate!')

    else:
        print('\033[0;31m Jogada Invalida!')