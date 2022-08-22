def fatorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


num = int(input(f'Degite um numero: '))
fat = fatorial(num)
#print(f'O fatorial de {num}! é {fat} ')
