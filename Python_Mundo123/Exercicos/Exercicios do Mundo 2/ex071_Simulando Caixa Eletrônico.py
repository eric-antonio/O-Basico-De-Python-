print('\033[1;37m='*50)
print('\033[1;33m{:^50}'.format('ATM-BIC'))
print('\033[1;37m=\033[m'*50)
print('{:^60}'.format('\033[1;32m Notas Disponiveis!\033[m'))
print('{:^57}'.format('\033[1;34m 100MT     200MT\033[m'))
print('{:^58}'.format('\033[1;34m 500MT     1000MT\033[m'))

valor =  int(input('Degite o valor de levantamento: '))
total = valor
ced = 1000
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Notas de {ced}MT Total: {totalced}')

        if ced == 1000:
            ced =500
        elif ced == 500:
            ced = 200
        elif ced == 200:
            ced = 100
        totalced = 0
        if total == 0:
            break
