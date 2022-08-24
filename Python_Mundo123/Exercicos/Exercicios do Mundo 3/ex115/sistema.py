from turtle import st
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
        #Vamos listar um arquivo txt
        arquivo.lerArquivo(arq)

    elif ans == 2:
        #Vamos cadastrar uma nova pessoa!
        interface.cabeçalho(f'\033[0;33m Novo Cadastro \033[m'.center(50))
        nome = str(input(f'Nome: ')).strip().lower().replace(' ','-')
        idade = interface.leiaInt(f'Idade: ')
        arquivo.cadastrar(arq, nome, idade)

    elif ans == 3:
        interface.cabeçalho(f'\033[0;33m Saindo do Sistema....\033[m')
        break

    else:
        interface.cabeçalho(f'\033[0;31m Erro- Digite uma op valida! \033[m')
        sleep(0.2)

