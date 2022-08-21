def leia(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m Erro Degite um numero inteiro valido.\033[m')
        if ok:
            break
    return valor


n = leia('Digite um numero: ')
print(f'Voce acabou de degitar o numero {n}')
