from  time import  sleep
def processando():
    for i in range(0, 8, 1):
        sleep(0.3)
        print(f'\033[0;33m.\033[m',end='')

    msg = 'Pocessando'
    print(f'\033[0;33m{msg}\033[m', end='')

    for i in range (0, 8, 1):
        sleep(0.3)
        print(f'\033[0;33m.\033[m',end='')
    print()
    print(f'\033[0;32m......Conclido com Sucesso!......\033[m')

def maior(*numeros):
    processando()
    cont = maior = 0
    print(f'Analisando os valores passsados!')
    sleep(0.2)
    for valor in numeros:
        print(f'{valor}', end=' ')
        sleep(0.1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.\n'
          f'O maior valor foi {maior}')


maior(1, 2, 4, 5, 6, 6, 7)
