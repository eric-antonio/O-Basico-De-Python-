from lib import interface
from time import sleep
from lib import arquivo

arq = 'BDex115.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    ans = interface.menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    # a variavel ans passa uma lista para o metodo menu que por sua vez permite a inserção de uma opção!
    if ans == 1:
        print(f'Op1')
    elif ans == 2:
        interface.cabeçalho(f'Op2')
    elif ans == 3:
        interface.cabeçalho(f'\033[0;33m Saindo do Sistema....\033[m')
        break
    else:
        interface.cabeçalho(f'\033[0;31m Erro- Digite uma op valida! \033[m')
        sleep(0.2)

