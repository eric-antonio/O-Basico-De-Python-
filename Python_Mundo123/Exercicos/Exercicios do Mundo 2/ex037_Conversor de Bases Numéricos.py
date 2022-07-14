numero = int(input('\033[0;33m Insira o valor inteiro que deseja converter:'))
base = int(input(' Para que base desja converter o valor? \033[m  \n'
                 '\033[0;32m ****************** \033[m \n'
                 '\033[0;34m 1-Binario \033[m \n'
                 '\033[0;35m 2-Octal \033[m \n'
                 '\033[0;36m 3-Hexadecimal \033[m \n'
                 '\033[0;32m ****************** : \033[m'))

if base == 1:

    print('\033[0;34m O resultado da conversão de {} deu {} \033[m'.format(numero,bin(numero)))

elif base == 2:

    print('\033[0;35m O resultado da conversão de {} deu {} \033[m'.format(numero,oct(numero)))

elif base == 3:

    print('\033[0;36m O resultado da conversão de {} deu {} \033[m'.format(numero,hex(numero)))

else:
    print('\033[0;31m Opção invalida: \033[m ')
