lista = list()
par = list()
impar = list()
while True:
    valor = int(input(f'Degite um valor: '))
    lista.append(valor)
    ans = str(input(f'Quer continuar? [S/N]: ')).lower()[0]

    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

    if ans == 'n':
        break

print('-'*30)
lista.sort()
print(f'Lista completa é : {lista}')
par.sort()
print(f'O valores pares encontrados foram : {par}')
impar.sort()
print(f'Os valores impar encontados foram: {impar}')
