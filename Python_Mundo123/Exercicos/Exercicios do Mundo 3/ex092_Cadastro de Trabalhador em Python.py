from datetime import datetime

trabalhador = dict()
nome = str(input(f'Nome: '))
trabalhador['Nome'] = nome
ano = int(input(f'Ano de Nascimento: '))

# Aqui estamos a usar ao ano corente!
idade = datetime.now().year - ano
trabalhador['Idade'] = idade

carteira = int(input(f'Carteira de Trabalhador (0 não tem): '))
trabalhador['ctps'] = carteira
if carteira == 0:
    print(f'*'*30)
    for k, v in trabalhador.items():
        print(f'- {k} = {v}')
elif carteira != 0:
    contrato = int(input(f'Ano de Contratação: '))
    trabalhador['Contratado/a'] = contrato
    salario = float(input(f'Salario: '))
    trabalhador['Salario'] = salario
    trabalhador['Aposentadoria'] = trabalhador['Idade'] + ((contrato + 35) - datetime.now().year)
    print(f'=-'*20)
    for k, v in trabalhador.items():
        print(f'- {k} = {v}')
