from time import sleep
def contador(i, f, p):
    
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'=-'*20)
    print(f'\033[0;33m Contagem de {i} até {f} de {p} em {p}\033[m')
    
    if i < f:

        cont = i
        while cont <= f:
            print(f' {cont}', end=' ',flush=True)
            sleep(0.2)
            cont += p
        print(f'Fim!')
    else:
        cont = i
        while cont >= f:
            print(f' {cont}', end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print(f'Fim!')


contador(0, 5, 2)
contador(4, 0, 1)
print(f'\033[0;34m Agora é sua vez!\033[m')
i = int(input(f'\033[0;32m Degite o inicio: \033[m'))
f = int(input(f'\033[0;32m Degite o fim: \033[m'))
p = int(input(f'\033[0;32m Degite o passo: \033[m'))
contador(i, f, p)