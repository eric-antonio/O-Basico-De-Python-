lista = list()
maior = 0
menor = 0
for i in range(0,5):
    lista.append(int(input(f'Insira o valor na posição {i}:')))
    if i == 0:
        maior = menor =lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(f'-'*30)
print(f'Voce degitou os valores :{lista}')
print(f'-'*30)
print(f'O maior foi {maior} nas posiçoes : ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()

print(f'O menor foi {menor} nas posiçoes : ',end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()