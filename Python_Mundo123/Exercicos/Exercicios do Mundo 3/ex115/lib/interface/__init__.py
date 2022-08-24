def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m Erro!-Digite um valor Inteiro! \n'
                  f'Dentro das opções dispostas acima! \033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31m O usuario não inseriu nehum dado! \033[m')
            continue
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt}'.center(40))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt(f'Sua opção: ')
    return opc

