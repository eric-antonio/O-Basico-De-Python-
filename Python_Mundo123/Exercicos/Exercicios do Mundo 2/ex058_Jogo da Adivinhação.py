from  random import  randint
from  time import  sleep
print('\033[0;36m Sou o seu Pc Vamos Jogar! \n'
      'Acabei de Pensar em um numero entre 0....10 \n'
      'Tente Advinhar.. \033[m')

rand= randint(0,10)
tentavivas = 0
resposta = 'S'

n = int(input('\033[0;32m Degite o seu Palpite: \033[m'))
while n != rand:
      if n < rand:
            print('\033[0;31m O valor que eu escolhi é maior que esse!')
      else:
            print('\033[0;31m O valor que eu escolhi é menor que esse!')
      n = int(input('\033[0;32m Degite o seu Palpite novamente: \033[m'))
      tentavivas+=1
sleep(1)
print('\033[0;34m Acertou Miseravel com {} tentativas '.format(tentavivas))