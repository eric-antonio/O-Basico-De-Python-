print('\033[0;34m=\033[m'*30)
print('\033[0;33m 10 Termos de uma PA\033[m')
print('\033[0;34m=\033[m'*30)
peimeiro = int(input('\033[0;32m Primeiro termo :\033[m'))
razao = int(input('\033[0;32m Razão :\033[m'))

decimo = peimeiro + (10 - 1) * razao
for i in range(peimeiro, decimo + razao, razao):
    print('{}'.format(i), end='-> ')
print('Acabou ')