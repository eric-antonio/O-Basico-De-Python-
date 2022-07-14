preco=float(input('Qual é o preço do produto"?:  '))
novo=preco-(preco*5/100)
desconto=preco*5/100
print('O produto custa {}Mt \n com um desconto de {}% \n agora custa {} Mt  '.format(preco,desconto,novo))
