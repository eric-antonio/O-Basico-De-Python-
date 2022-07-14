res = 'S'
quantidade = soma = media = maior = menor = 0
while res in 'Ss':
    num = int(input('Degite um numero: '))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / quantidade
print('A media foi de {} e foram inseridos {} numeros '.format(media, quantidade))
print('O Maior valor foi de: {} \n'
      'O Menor foi de: {} '.format(maior, menor))
print('Acabou!...')
