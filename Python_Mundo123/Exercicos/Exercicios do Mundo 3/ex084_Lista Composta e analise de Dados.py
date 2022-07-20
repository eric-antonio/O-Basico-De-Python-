temp =[]
princ = []
maior = menor = 0
while True:
    temp.append(str(input(f'Nome: ')))
    temp.append(float(input(f'Peso: ')))

    #No bloco asseguir comparamos o maior e o menor peso.
    #Esse processo é feito na lista temp.
    
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor: 
            menor = temp[1]

    princ.append(temp[:])
    #Temos que fazer uma copia ou seja passar
    # os valores da lista para a nossa matriz.
    # em seguida devemos dar um clear() para que os valores não se 
    # repitam!
    temp.clear() #aqui esvaziamos a memoria da nossa lista!
    ans = str(input(f'Quer continuar? [S/N]: ')).upper()[0]


    if ans in 'N':
        break
print(f'='*30)
print(f'Ao todo foram cadastradas {len(princ)}')
print(f'O maior pesso foi de {maior}Kg', end=' ')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor pesso foi de {menor}Kg', end=' ')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print()
#print(f'\033[0;34m  {princ} \033[m')