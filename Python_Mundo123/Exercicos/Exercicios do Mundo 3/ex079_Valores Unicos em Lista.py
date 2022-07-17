lista = list()

while True:
    n =int(input(f'Degite um valor: '))
    if n not in lista:
        lista.append(n)
        print(f'\033[0;32m Valor Adiconado com Sucesso!\033[m')
    else:
        print(f'\033[0;31m Valor Duplicado!\n'
              f'Não sera adicionado!\033[m')
    resposta = str(input(f'Quer continuar? [N/S] :')).upper()[0]
    if resposta == 'N':
        break
lista.sort()
print(f'Voce degitou os valores : {lista}')