cont = ('zero', 'um',  'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'ónze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete','dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('\033[0;33m Degite um numero entre : 0 e 20:\033[m '))
    if 0 <= num <= 20 :
        break
    print('\033[0;31m Tente novamente.\033[m')
print(f'\033[0;36m O numero digitando por você foi {cont[num]} \033[m')

while True:
    res = str(input('\033[0;34m Você quer continuar?\033[m\n'
                        '\033[0;35m Sim-S / Não- N:  \033[m')).upper().strip()[0]
    if res =='S':
        while True:
            num = int(input('\033[0;33m Degite um numero entre : 0 e 20:\033[m '))
            if 0 <= num <= 20:
                break
            print('\033[0;31m Tente novamente.\033[m ')
        print(f'\033[0;36m O novo numero digitando por você foi {cont[num]} \033[m')
    else:
        break
        print('\033[0;31m Degite a opção coreta!.\033[m ')



print(f'\033[0;36m O ultimo numero digitando por você foi {cont[num]} \033[m')