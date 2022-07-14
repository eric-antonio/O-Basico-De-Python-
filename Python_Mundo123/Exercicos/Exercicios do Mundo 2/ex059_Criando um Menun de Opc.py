from time import  sleep
valor1 = int(input('\033[0;34m Insira o primeiro valor: \033[m'))
valor2 = int(input('\033[0;34mInsira o segundo valor: \033[m'))
op = 0
soma = 0
while op != 5:
    print('*'*20)
    print('\033[0;33m'
          ' 1- Somar\n'
          ' 2- Multiplicar\n'
          ' 3- Consultar o Maior\n'
          ' 4- Novos Numeros\n'
          ' 5- Sair do Programa! '
          '\033[m')
    print('*'*20)
    op = int(input(' \033[0;34m Insira a opção desejada: '))

    if op == 1:
        soma = valor1 + valor2
        print('\033[0;35m O resultado da soma de {} e {} foi {} \033[m'.format(valor1,valor2,soma))
    elif op == 2:
        mult = valor1 * valor2
        print('\033[0;35m O resultado da multilicação de {} e {} foi {} \033[m'.format(valor1,valor2,soma))
    elif op == 3:
        maior =0
        if valor1 < valor2:
            maior =valor2
            print('\033[0;35m O maior valor é {} \033[m'.format(maior))
        elif valor1 > valor2:
            maior = valor1
            print('\033[0;35m O maior valor é {} \033[m'.format(maior))
        else:
            print('\033[0;35m Os valores são semelhantes {} e {} \033[m'.format(valor1,valor2))
    elif op == 4:
        print('\033[0;32m **********Insira os novos valores****** \033[m')
        valor1 = int(input('\033[0;33m Insira primeiro valor: \033[m'))
        valor2 = int(input('\033[0;33m Insira o segundo valor: \033[m '))
    elif op > 5:
        print('\033[0;31m ERRO 4422 ( ERRO DE DEGITAÇÃO ) \n '
              'Tente novamente..... \033[m ')

sleep(0.5)
print('Muito Obrigado Volte Sempre')