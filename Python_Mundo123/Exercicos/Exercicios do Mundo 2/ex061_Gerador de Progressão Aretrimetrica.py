print('\033[0;33m=\033[m'*30)
print('\033[0;34m Gerador de P.A \033[m')
print('\033[0;33m=\033[m'*30)
peimeiro = int(input('\033[0;32m Primeiro termo :\033[m'))
razao = int(input('\033[0;32m Razão :\033[m'))
termo =  peimeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont += 1
print('\033[0;35m Fim!')
