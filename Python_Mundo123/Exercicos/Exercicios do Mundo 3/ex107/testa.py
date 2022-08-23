import moeda
p = float(input(f'Degite o preco (MT): '))
print(f'A metade de é {moeda.metade(p)} \n'
      f'O dobro de é {moeda.dobro(p)}\n'
      f'Aumentando 10% temos {moeda.aumentar(p, 10)}\n'
      f'Diminuindo 10% temos {moeda.diminuir(p, 10)}')
