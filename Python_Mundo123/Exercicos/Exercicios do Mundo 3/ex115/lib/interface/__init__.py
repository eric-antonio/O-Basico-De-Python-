
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

