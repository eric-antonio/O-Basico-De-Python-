from time import sleep

print('-='*20)
print('Analisandor de Triangulos')
print('-='*20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Analisando...')
    sleep(3)
    print('Os segmentos a cima podem formar um Triangulo!')
else:
    print('Os segmentos a cima não podem formar um Triangulo!')


