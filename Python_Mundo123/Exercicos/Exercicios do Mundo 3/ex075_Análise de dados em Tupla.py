#Em python por meio de uma gambiar é possivel
# definir os valores de uma tupla pela Inteface
# Exemplo:
tupla = (int(input(f'Degite o primeiro:')),
     int(input(f'Degite o segundo:')),
     int(input(f'Degite o terceiro:')),
     int(input(f'Degite o quarto:')))
#Parte 01
if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes!')
else:
    print(f'Não foi inserido o valor 9 ')

#Parte 02
if 3 in tupla:
    print(f'O primeiro valor 3 foi degitado na posição {tupla.index(3)+1}')
else:
    print(f' Não foi inserido o valor 3')

#Parte 03
print(f'Os valores pares digitados: ', end='')

for i in tupla:
    if i % 2 == 0:
        print(f' {i}', end='')

print(f'\n Voce digitpu os valores : {tupla}')