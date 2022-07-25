ficha = list()

while True:
    nome = str(input(f'Insira o nome: '))
    nota1 = float(input(f' O/A estudante {nome} na 1 avaliação teve: '))
    nota2 = float(input(f' O/A estudante {nome} na 2 avaliação teve: '))
    nota3 = float(input(f' O/A estudante {nome} na 3 avaliação teve: '))
    media = (nota1 + nota2 + nota3) / 3
    ficha.append([nome, [nota1, nota2, nota3], media])

    ans = str(input(f'Quer continuar a cadastrar estudantes? [S/N]: ')).upper()[0]
    if ans in 'Nn':
        break
for i, e in enumerate(ficha):
    print(f'{e}', end='')

print(f'Chegou!!!!!')
