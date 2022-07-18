lista = list()

for i in range(0, 5):
    n = int(input(f'\033[0;32m Degite um valor: \033[m'))
    if i == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'-'*30)
print(f'Os valores digitados  em ordem foram {lista}')