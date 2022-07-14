soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input('Insira o valor nr {}: '.format(i)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('Voce degitou {} numeros pares e a soma de {}'.format(cont,soma))
