def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31m Erro!-Digite um valor Inteiro! \033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31m O usuario não inseriu nehum dado! \033[m')
            continue
            return 0
        else:
            return n


def linha(tam=40):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt}'.center(30))
    print(linha())


def menu(lista):
    cabeçalho('\033[0;34m MENU PRINCIPAL \033[m')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;32m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt(f'Sua opção: ')
    return opc

