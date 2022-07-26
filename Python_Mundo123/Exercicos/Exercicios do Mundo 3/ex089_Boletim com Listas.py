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

print('-='*30)
print(f'{"No.":<4}{"Nome:":<10}{"Media:":>8}')
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:8.1f}')

while True:
    print(f'-'*35)
    op= int(input(f'Mostrar notas de qual alno? \n (Degitando 999 o progrma insera! )'))
    if op == 999:
        print(f'Finalizando!...')
        break
    if op <= len(ficha):
        print(f'Notas de {ficha[op][0]} sao {cad[op][1]}')

print(f'Chegou!!!!!')
