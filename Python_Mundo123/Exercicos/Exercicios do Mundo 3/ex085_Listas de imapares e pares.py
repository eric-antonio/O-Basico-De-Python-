num = [[], []]
valor = 0

for i in range(1, 8):
    valor = int(input(f'Insira um valor na posição {i}: '))

    if valor % 2 == 0:
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()
print(f'-'*30)
print(f' Os valores pares são {num[0]} \n E os valores imapres são {num[1]}')