from time import sleep
from lib import arquivo 
from lib import interface


arq = 'BD_Gestão_D_Professores!'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    ans = interface.menu(['Cadastrar Professor', 'Ver Professores', 'Sair...'])

    if ans == 1:
        interface.cabeçalho('OP1')
        #arquivo.lerArquivo(arq)
    elif ans == 2:
        interface.cabeçalho('OP2')
    elif ans == 3:
        interface.cabeçalho('op3')
        break
    else:
        interface.cabeçalho(f'\033[0;31m Erro- Digite uma op valida! \033[m')
        sleep(0.2)
