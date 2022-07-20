teste =list()
teste.append('Éric António')
teste.append(22)

pessoa = list()
pessoa.append(teste[:])

teste[0] ='Milena'
teste[1] =22
pessoa.append(teste[:])
#print(pessoa)


grupo = [['Eric', 22], ['Asten', 22], ['Yara', 22], ['Agostinho', 21]]
for p in grupo:
    print(f'{p[0]} tem {p[1]}')


dados = list()
menbro = list()

for i in range(0, 5):
    dados.append(str(input(f'Nome: ')))
    dados.append(int(input(f'Idade: ')))
    menbro.append(dados[:])# copiando os dados da lista para á matriz!
    dados.clear()# Como ja foi efectuadada a copia
    # dos dados para a matriz menbro pode-se apagar a anterior sem problemas!
print(dados)
print(menbro)
# Exibindo so maiores de 21 e menores de 18
for p in menbro:
    if p[1] >= 21:
        print(f' {p[0]} tem {p[1]} anos de idade!')
        print(f'\033[0;32m Jovem!\033[m')
    elif p[1] < 18:
         print(f' {p[0]} tem {p[1]} anos de idade!')
         print(f'\033[0;31m Adolescente! \033[m')