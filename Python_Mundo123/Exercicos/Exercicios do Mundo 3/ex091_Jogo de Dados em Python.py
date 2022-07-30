from random import randint
from  time import sleep
from  operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
""" Na linha a baixo usamos um novon dicionario para 
    aplicar o sortetd. Porem a intenção é ordenar pelos valores 
    e não pelas chaves. Importamos a biblioteca (itemgetter) para 
    que assi fosse possivel selecionar o intem ou seja o valor que teremos 
    como referencia para ordenar!
    o (reverse=True )serve para exibir do maior ao menor!
    EX: JOGADOR tem o indice 0 entao usamos o 1 pois todos o valores estão nesse indice!
    """
ranking = sorted(jogo.items(), key=itemgetter(1))
print('='*30)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar {v[0]} com {v[1]}')
    sleep(0.5)
