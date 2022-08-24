from lib import interface
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        interface.cabeçalho(f'Houve um Erro! Na crição do Arquivo.')
    else:
        interface.cabeçalho(f'Arquivo! {nome} Criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        interface.cabeçalho(f'ERRO AO LER O ARQUIVO'.center(30))
    else:
        interface.cabeçalho(f'\033[0;32m Pessoas Cadastradas \033[m')
        #print(a.read())- exibe todo o documento sem colocar em uma tupla!
        #print(a.readlines())- é uma opção onde mostra os dados em forma de tupla!
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>2} anos')
    finally:
        a.close


def cadastrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        interface.cabeçalho(f'Cagou tudo Brooo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print(f'\033[0;31m Não consegiu registar Bugou!!!!\033[m ')
        else:
            interface.cabeçalho(f'\033[0;32m Novo registro {nome} Adicionado! \033[m')
            a.close()
    finally:
        a.close()
