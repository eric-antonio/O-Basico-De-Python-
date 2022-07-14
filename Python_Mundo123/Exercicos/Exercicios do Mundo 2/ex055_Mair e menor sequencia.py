maior = 0
menor = 0

for i in range(1,6):
    peso=float(input('Insira o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior pesso lido foi de {}kg'.format(maior))
print('O menor pesso lido foi de {}kg'.format(menor))