try:
    a = int(input(f'Degite um numero:'))
    b = int(input(f'Degite um numero: '))
    r = a / b
except:
    print(f'Infelizmente tivemos um problema!'
          f'Reveja o Código!')
else:
    print(f'O reso;tade de {a} / {b} = {r:.1f}')
    