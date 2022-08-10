pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input(f'Nome: '))
    while True:
        pessoa['Sexo'] = str(input(f'Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print(f'\033[0;31m ERRO! Degite somente as opções disponiveis!\033[m ')
    pessoa['Idade'] = int(input(f'Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        ans =str(input(f'Quer Continuar?[S/N]: ')).upper()[0]
        if ans in 'SN':
            break
        print('\033[0;31m Erro! Responda com S ou N\033[m')
    if ans == 'N':
        break
print(f'-='*10)
print(f'Ao todo temos {len(galera)} pessoas Cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos ')
print(f'As Mulheres  cadastradas foram ', end='')
for p in  galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ;', end='')
print()
print('Lista das Pessoas acima da media: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print(f'    ')
        for k, v in p.items():
            print(f' {k} = {v} ', end='')
        print()
