def ficha(jog='<Desconhecido>', gol=0):
    print('-'*30)
    print(f' O jogador {jog} fez {gol} no campeonato')



n = str(input(f'Nome do jogador: '))
g = str(input(f'Golos:'))
if g.isnumeric():
     g = int(g)
else:
     g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)