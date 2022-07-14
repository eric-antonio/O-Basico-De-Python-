print('\033[0;35m{:=^40}'.format(' Lojas Marvolas '))
preco = float(input('\033[0;34m Valor das compras: '))
print('''\033[0;33m Formas de Pagamento: 
1- á vista dinheiro/cheque
2- á vista cartão
3- 2x no cartão
4- 3x ou mais no cartão \033[m''')
opcao =  int(input('Dedite a opcao desejada: '))

if opcao == 1:
    total =  preco - (preco * 10 / 100)
elif opcao ==2:
    total =  preco - (preco * 5 / 100)
elif opcao ==3:
    total =  preco
    parcela = total / 2
    print('\033[0;34m A sua compra sera parcelada duas vezes(2x) e pagara {}MT no final! \033[m'.format(preco,parcela))
elif opcao ==4:
    total =  preco + (preco * 20 / 100)
    totalparc = int(input('\033[0;33m Quantas Parcelas?: '))
    parcela =  total / totalparc
    print('\033[0;34m A sua compra sera parcelada em {}x de {:.2f} Com Juros \033[m'.format(totalparc,parcela))
else:
    total= preco
    print('\033[0;31m Opcao Ivalida de pagamento!')
print('\033[0;32m A sua compra de {:.2f}MT vai custar {}MT no final! \033[m'.format(preco,total))