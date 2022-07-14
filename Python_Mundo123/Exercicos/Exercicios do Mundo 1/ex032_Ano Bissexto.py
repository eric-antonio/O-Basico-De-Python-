from  datetime import  date
ano=int(input('Insira o ano que deseja analisar? \n Para analisar o ano actual degiste 0:'))
if ano==0:
    ano=date.today().year
    print('Estamos em {}'.format(ano))

if ano%4==0 and ano % 100 !=0 or ano % 400 ==0 :
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {}  Não é Bissexto!'.format(ano))