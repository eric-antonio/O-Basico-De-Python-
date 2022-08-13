def area():
    print(f'Controle de Terrenos')
    print('-'*20)
    l = float(input(f' Largura (m): '))
    c = float(input(f'Comprimento (m): '))
    a = l * c
    print(f' A área de terreno {l:.1f} x {c:.1f} é de {a}m^2')


area()