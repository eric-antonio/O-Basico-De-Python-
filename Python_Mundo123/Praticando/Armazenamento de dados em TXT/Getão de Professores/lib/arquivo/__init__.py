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