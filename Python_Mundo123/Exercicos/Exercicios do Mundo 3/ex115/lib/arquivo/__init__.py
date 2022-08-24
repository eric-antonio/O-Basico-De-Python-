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

