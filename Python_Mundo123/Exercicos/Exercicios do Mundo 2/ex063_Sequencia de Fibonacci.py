print('\033[0;32m-*-'*15)
print('\033[0;33m Sequencia de FIbonacci')
print('\033[0;32m-*-'*15)
n = int(input('\033[0;33m Quantos termos você quer mostrar?:\033[m '))
t1 = 0
t2 = 1
print('\033[0;32m-*- \033[m'*15)
print('{} -> {} '.format(t1, t2), end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\033[0;32m Fim!')
