listagem = ('Lápis ', 3.5,
            'Borrcha',2.5, 
            'Caderno', 15.4,
            'Estojo', 10.5,
            'Traferidor',13.5,
            'Compasso', 12.5,
            'Pasta', 18.5,
            'Canetas', 3.5,
            'Livros', 25.5)
# :.<30 vai alinhar a esquerda com Pontinhos a direita 
print(f'Listagem de Preços'.center(40,'*'))
for pos in range(0,len(listagem)):
    if pos % 2 == 0: 
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'{listagem[pos]:>2}MT')
print(f'-'*40)