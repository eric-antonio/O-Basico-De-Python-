def fatorial(num=1):
    f = 1
    for i in range(num, 0, -1):
        f *= i
    return f

n = int(input(f' Degite um numero: '))
print(f'O factorial de {n} é {fatorial(n)}')
