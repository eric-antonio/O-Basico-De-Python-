
c = ('\033[0;31m',
     '\033[0;32m',
     '\033[0;33m',
     '\033[0;34m',
     '\033[0;35m',
     '\033[0;36m')

def ajuda(com):
    help(com)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-'*tam)
    print(f' {msg}')
    print('-' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp',2 )
    comando = str(input(f'Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else: ajuda(comando)
    titulo('Termino da Biblioteca!', 1)