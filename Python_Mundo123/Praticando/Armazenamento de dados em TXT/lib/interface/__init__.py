#---Menu----
def menu(lista):
    # um contador para nos ajudar a idicar as opções!
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt(f'Digite a sua opção: ')

    return opc


#----Linha-----
def linha(tam=40):
    print('-'*tam)


#----LeiaInt----

