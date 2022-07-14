print('\033[1;36m-'*40)
print('    \033[1;33m SUPER MERCADO MARVOLAS\033[m    ')
print('\033[1;36m-\033[m'*40)
total = menor  = maior = cont  = totmil = 0
nomedomaiscarro = nomebarato = ''
while True:
    nome = str(input('\033[1;30m Nome do Produto: '))
    preco = float(input(' Preço: \033[m'))
    cont += 1
    total += preco

    if preco > 1000:
        totmil +=1
        maior = preco
        nomedomaiscarro=nome

    if cont == 1 or preco <menor:
        menor = preco
        nomebarato =nome

    ans = ' '
    while ans not in 'SN':
        ans = str(input('\033[1;34m Deseja comprar mais produtos?:\033[m ')).strip().upper()[0]

    if ans == 'N':
        break

print(f'\033[1;30m O total da sua compra foi de:\033[m \033[1;31m{total}MT\n'
      f'\033[1;30m O produto mais carro foi:\033[m\033[1;32m {nomedomaiscarro} \033[m \033[1;30m e custou:\033[m\033[1;31m{maior}MT \n'
      f'\033[1;30m O mais barrato foi \033[m \033[1;32m{nomebarato}\033[m\033[1;30m e custou:\033[m\033[1;31m{menor} ')