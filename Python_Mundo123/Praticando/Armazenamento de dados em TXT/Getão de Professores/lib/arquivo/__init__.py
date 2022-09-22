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


#----Ler Arquivo-------
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
        a.close()


#-----Cdastras no arquivo-----
def cadstrar(arq, nome='<Desconhecido>', idade=0):
    try:
        a = open(arq,'at')
    except:
        interface.cabeçalho(f'\033[0;31m Não foi possivel localizar o Arquivo de resgistro! \033[m')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            interface.cabeçalho(f'\033[0;31m Não consegiu registar Bugou!!!!\033[m ')
        else:
            interface.cabeçalho(f'\033[0;32m Novo registro {nome} Adicionado! \033[m')
            a.close()
        finally:
            a.close()
