from time import  sleep
c = ('\033[0;31m',
     '\033[0;32m',
     '\033[0;33m',
     '\033[0;34m',
     '\033[0;35m',
     '\033[0;36m',
     '\033[7;30')

def ajuda(com):
    titulo(f'Acessando o manul do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-'*tam)
    print(f' {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp ', 2)
    comando = str(input(f'\033[m Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
    titulo('Termino da Biblioteca!', 1)
