numero = int(input('Degite um número: '))
tot=0
for i in range (1,numero+1):
    if numero % i == 0:
        print('\033[0;33m ', end='')
        tot +=1
    else:
        print('\033[0;31m ', end='')
    print('{} '.format(i), end='')
print('\n \033[m O número {} foi divisivel {} vezes'.format(numero,tot))

if tot == 2:
    print('É primo ')
else:
    print('Não é primo')