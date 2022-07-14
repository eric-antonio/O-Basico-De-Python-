cont = 1
tabuada = 0
while True:
    n = int(input('Quer a Tabuada de que valor?: '))
    if n <0:
        break

    while cont <=12:
        tabuada = n * cont
        print(f' {n} * {cont} = {tabuada}')
        cont += 1
    cont = 1

print('Acabou....\n'
      'Volte Sempre!')