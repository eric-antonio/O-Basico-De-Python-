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
print('-'*30)
print(f' Cod', end='')
for i in jogador.keys():
    print(f'{i:>6} ', end='')
print()
print(f'-'*30)
for k, v in enumerate(equipe):
    print(f' {k+1:>3}º ', end='')
    for d in v.values():
        print(f' {str(d):<10} ', end='')
    print()
print(f'-='*10)


"""print(f'O jogador {jogador["Nome"]} Jogou {len(jogador["Golos"])} jogos! ')
for i, v in enumerate(jogador["Golos"]):
    print(f' No {i+1}º jogo fez {v} Golos!')
print(f'Foi um total de {jogador["Total G"]}')"""