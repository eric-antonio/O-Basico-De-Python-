jogador = dict()
golos = list()
jogador['Nome'] = str(input(f'Insira o nome do Jogador: '))
jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou?: '))
total = 0
for i in range(0, jogos):
    golos.append(int(input(f'Quantos golos na partida? -{i+1}: ')))
jogador['Golos'] = golos
jogador['Total G'] = sum(golos)
print(f'-='*10)
print(jogador)
print(f'-='*10)

for k, v in jogador.items():
    print(f'O campo \033[0;33m {k}\033[m tem valor \033[0;34m {v} \033[m')
print(f'-='*10)
print(f'O Jogador {jogador["Nome"]} jogou {jogos} jogos!')
for i, v in enumerate(golos):
    print(f' No jogo {i+1 }, fez {v} golos!')
print(f'Foi um total de {jogador["Total G"]} Golos!')
