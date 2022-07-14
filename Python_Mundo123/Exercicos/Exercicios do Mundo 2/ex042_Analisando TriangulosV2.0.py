from time import sleep

print('\033[0;32m-= \033[m'*20)
print('\033[0;33m Analisandor de Triangulos \033[m')
print('\033[0;32m-= \033[m'*20)
r1 = float(input('\033[0;33m Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: \033[m '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[0;34m Analisando...\033[m')
    sleep(3)
    print('\033[0;35m Os segmentos a cima podem formar um Triangulo!\033[m', end='')
    if r1 == r2 == r3:
        print('\033[0;36m Equilatero!')
    elif r1 != r2 != r3 != r1:
        print('\033[0;36m Escaleno!')
    else:
        print('\033[0;36m Isosceles!')
else:
    print('\033[0;31m Os segmentos a cima não podem formar um Triangulo!')