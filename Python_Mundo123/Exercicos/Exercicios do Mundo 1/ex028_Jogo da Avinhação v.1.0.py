from  random import  randint
from  time import sleep
#Escreva um programa que faça o computador ""pensar" em
# um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
# qual foi o numero escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

computador=randint(0,5)
jogo=int(input('Oi quer jogar? \n'
      'Sim! Degite 1\n'
      'Não! Degite 2\n'
    'Vamos? : '))

if jogo==1:

    print('Vou pensar em um numero tente advinhar!\n'
          '..........Pensando........')
    sleep(3)
    print('Já pensei agora tente!')

    jogador=int(input('Insira um numero: '))
    if jogador== computador:
        print('Pensei no número {} \nvocê acertou! Parabens!'.format(computador))
    else:
        print('Pensei no número {} \n'
              'você Errou! Tente Novamente!'.format(computador))
elif jogo==2:
    print('Vou Jogar com outra pessoa!')
else:
    print('Era só ter dito sim ou não!')


