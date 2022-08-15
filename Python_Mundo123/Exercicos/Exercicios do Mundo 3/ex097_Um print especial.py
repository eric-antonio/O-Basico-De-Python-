def escreva(msg):
    tam = len(msg)+4
    print('~'*tam)
    print(msg.center(5))
    print('~'*tam)

#Program pricipal
msg = str(input(f'Insira um texto: '))
escreva(msg)
