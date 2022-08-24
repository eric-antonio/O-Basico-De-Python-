try:
    a = int(input(f'Degite um numero:'))
    b = int(input(f'Degite um numero: '))
    r = a / b
except (ValueError, TypeError):
    print(f'\033[031m Tivemos um problema com os tipos de dados\033[m')
except ZeroDivisionError:
    print('\033[031m Não é possivel dividir por Zero!\033[m')
except KeyboardInterrupt:
    print(f'\033[031m O usuario não introduziu os dados!\033[m')
except Exception as erro:
    print(f'O erro encomtado foi {erro.__cause__}')
else:
    print(f'\033[033m  {a} / {b} = {r:.1f}\033[m')
finally:
    print(f'Desenvolvido por: \033[0;35m https://gitHub.com/eric-antonio\033[m')
