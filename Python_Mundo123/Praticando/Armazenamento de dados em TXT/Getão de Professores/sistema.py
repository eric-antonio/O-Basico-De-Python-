from time import sleep
from lib import arquivo 
from lib import interface


arq = 'BD_Gestão_D_Professores!'
if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)


while True:
    ans = interface.menu(['Cadastrar Professor', 'Ver Professores', 'Sair...'])

    if ans == 1:
        #Vamos cadastrar os Professores!
        interface.cabeçalho(f'\033[0;33m Novo Cadastro! \033[m'.center(50))
        nome = str(input(f'Nome: ')).strip().lower().replace(' ', '-')
        idade = interface.leiaInt(f'Idade: ')
        instituição = str(input(f'Instituição de Ensino: ')).strip().lower().replace(' ', '-')
        disciplina = str(input(f'Disciplina de: ')).strip().lower().replace(' ', '-')
        cargaHoraria = interface.leiaInt(f'Carga Horaria semanal: ')
        salario = 1500 * cargaHoraria
        arquivo.cadstrar(arq, nome, idade, instituição, disciplina, cargaHoraria, salario)

    elif ans == 2:
        interface.cabeçalho('OP2')
    elif ans == 3:
        interface.cabeçalho(f'\033[0;33m Saindo do Sistema....\033[m')
        break
    else:
        interface.cabeçalho(f'\033[0;31m Erro- Digite uma op valida! \033[m')
        sleep(0.2)
