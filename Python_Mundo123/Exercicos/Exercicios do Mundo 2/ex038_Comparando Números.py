n1 = int(input('\033[0;33m Insira o primeiro Numero: '))
n2 = int(input('Insira o Segundo Numero:\033[m'))

if n1 > n2:
    print('O numero {} é o maior!'.format(n1))
elif n2 > n1:
    print('O numero {} é o maior!'.format(n2))
elif n1 == n2:
    print('Os numeros são iguais!')
