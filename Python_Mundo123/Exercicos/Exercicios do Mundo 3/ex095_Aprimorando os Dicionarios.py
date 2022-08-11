jogador = dict()
golos = list()
equipe = list()

while True:
    jogador.clear()
    golos.clear()
    jogador['Nome'] = str(input(f'Nome do Jogador: '))
    tot = int(input(f'Quatos jogos fez o {jogador["Nome"]}?: '))
    for i in  range(0, tot):
        golos.append(int(input(f'Quantos golos no {i+1}º jogo?: ')))
    jogador['Golos'] = golos[:]
    jogador['Total G'] = sum(golos)
    equipe.append(jogador.copy())
    while True:
        ans = str(input(f'Quer continuar? [S/N]')).upper()[0]
        if ans in 'S/N':
            break
        print('\033[0;31m     Erro 4422! \n \033[0;33m Responda com S ou N.\033[m')
    if ans == 'N':
        break
print('-'*40)
print(f' Cod', end='')
for i in jogador.keys():
    print(f'{i:>10} ', end='')
print()
print(f'-'*40)
for k, v in enumerate(equipe):
    print(f' {k+1:>3}º ', end='')
    for d in v.values():
        print(f' {str(d):<15} ', end='')
    print()
print(f'-='*20)
while True:
    busca = int(input(f'\033[0;32m Mostrar Dados de qual Jogador? \033[0;33m \n-Degite 999 para terminar:\033[m '))
    if busca == 999:
        break
    if busca >= len(equipe):
        print(f'\033[0;31m Erro! Player do not Exists!')
    else:
        print(f'\033[0;34m ---- LEVANTAMENTO DO JOGADOR {equipe[busca]["Nome"]}! ---\033[m')
        for i, g in enumerate(equipe[busca]['Golos']):
            print(f'No jogo {i+1}º fez {g} Golos!')
    print(f'-='*30)

