matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insira um valor na posição {l},{c} : '))


print(f'-'*30)

print(f'------------Matriz---------')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        #Aqui efetuamos a soma de todos os valores pares da nossa Matriz!
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'-'*30)
print(f'A soma dos valores pares é {spar}')

#A soma dos valores da 3 coluna .
# é gfeito um for para percorer a linha não a
# coluna.
# l= 0 [1] [2] [3]
# l= 1 [4] [5] [6]
# l= 2 [7] [8] [9]
#      c=0 c=1 c=2
# A gora que sabemos que o indice da 3-Terceira coluna é 2
# podemos fixar o indice e somente percorer as linhas com o uso de apenas um ciclo.
# Ficando assim : scol += matriz[l][2] , a linha 'l' sera incrementada a cada ciclo!
for l in range(0, 3):
    scol += matriz[l][2]
print(f' A soma dos valores da 3 coluna é {scol}')

#Agora remos verificar o maior elemento da segunda linha!
# sabemos que o indice da seguda linha é o indice 1.
# logo iremos apenas nos focar na linha 1 e percorer as colunas!
# Usando assim a expressão: mai = matriz[1][i]
# l= 0 [] [] []
# l= 1 [4] [5] [6]
# l= 2 [] [] []
for i in range(0, 3):
    if i == 0:
        mai = matriz[1][i]
    elif matriz[1][i] > mai:
        mai = matriz[1][i]
print(f'O maior foi {mai}')