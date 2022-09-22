#---leia int----
def leiaInt(val):
    while True:
        try:
            numero = int(input(val))
        except (ValueError, TypeError):
            print(f'\033[0;31m Erro!-Digite um valor Inteiro! \033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31m O usuario não inseriu nehum dado! \033[m')
        continue
        return 0
    else:
        return n


#---linha
def linha(tam=50):
    return '-' * tam


#---rodape---
def rodape(txt):
    print(linha())
    print(f'{txt}'.center(40))
    print(linha())


#-----menu----
def menu(lista):
    rodape('\033[0;34m MENU PRINCIPAL \033[m')
    c = 1
    for item in lista:
        print(f'\033[0;33m {c} \033m - \033[0;34m {item}\033[m')
        c += 1
    print(linha())
    opc =leiaInt(f'Selecione uma opção:')
    return opc
