def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31m Erro Digite um numero Inteiro valido.\033[m')
        except (KeyboardInterrupt):
            print(f'Entrada de dados enteropida pelo Usuario!')
            # a linha a baixo fara com que o
            # programa volte para o while!
            return 0
            continue
        else:
            return n


def leaiFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m Erro!\n'
                  f'Digite um numero Float Valido!\033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31m O usuario não inseriu nehum dado.')
            return 0
            continue
        else:
            return n


num = leiaInt(f'Degite um  Inreiro valor: ')
f = leaiFloat(f'Digite um Float : ')
print(f'O valor digitado foi {num}')
print(f'O valor digitado foi {f}')

