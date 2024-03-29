#----LeiaInt----
def leiaInt(val):
    while True:
        try:
            n = int(input(val))
        except (ValueError, TypeError):
            print(f'\033[0;31m Erro!-Digite um valor numerico do sem casa decimais! \033[m')
        except (KeyboardInterrupt):
            print(f'\033[0;31m O usuario não inseriu nehum dado! \033[0m')
            continue
            return 0 
        else:
            return n



#----Linha-----
def linha(tam=40):
    return '-' * tam


#----Caveçalho----
def cabeçalho(txt):
    print(linha())
    print(f'{txt}'.center(30))
    print(linha())



#---Menu----
def menu(lista):
    # um contador para nos ajudar a idicar as opções!
    cabeçalho('\033[0;34m Sistema de Geão de Professores \033[m'.center(40))
    c = 1
    
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt(f'Digite a sua opção: ')
    return opc

