from lib import interface
#----Verficar se o arquivo exixte-----
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except ( FileExistsError, FileNotFoundError):
        return False
    else:
        return True


#-----Criar Arquivo-----
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        interface.cabeçalho(f'\033[0;31m Houve um Erro! Na crição do Arquivo.\033[m')
    else:
        interface.cabeçalho(f'\033[0;32m Arquivo! {nome} Criado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        interface.cabeçalho(f'\033[0;31m ERRO AO LER O ARQUIVO\033[m'.center(30))
    else:
        interface.cabeçalho(f'\003[0;33m  Professores Cdastrados \033[m')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} - {dado[1]:>2} {dado[2]:>}')
    finally:
        a.close
