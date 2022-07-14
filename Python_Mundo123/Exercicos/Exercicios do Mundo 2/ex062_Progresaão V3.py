peimeiro = int(input('\033[0;32m Primeiro termo :\033[m'))
razao = int(input('\033[0;32m Razão :\033[m'))
termo =  peimeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += razao
        cont += 1
    print('\033[0;32m Pausa!\033[m')
    mais = int(input('Quantos mais deseja mostrar:\033[m'))


print('\033[0;33m Progressao realizada com {} termos mostrados Fim!\033[m'.format(total))