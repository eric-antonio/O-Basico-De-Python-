from time import sleep
from lib import interface

while True:
    ans = interface.menu(['Cadastrar Professor', 'Ver Professores', 'Sair...'])

    if ans == 1:
        interface.cabeçalho('OP1')
    elif ans == 2:
        interface.cabeçalho('OP2')
    elif ans == 3:
        interface.cabeçalho('op3')
        break
    else:
        interface.cabeçalho(f'\033[0;31m Erro- Digite uma op valida! \033[m')
        sleep(0.2)