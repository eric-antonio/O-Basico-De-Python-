from uteis import *

"""
      Em caso de comflito de importações ou existam modulos com 
      mesmas funções recomenda-se a usar essa foema de importar:
            
            import uteis
      
            num = int(input(f'Degite um numero: '))
            fat = uteis.fatorial(num)
            print(f'O fatorial de {num}! é {fat} \n'
                  f'O dobro do {num} é {uteis.dobro(num)}\n'
                  f'O triplo de {num} é {uteis.triplo(num)}')
      
"""

num = int(input(f'Degite um numero: '))
fat = fatorial(num)
print(f'O fatorial de {num}! é {fat} \n'
      f'O dobro do {num} é {dobro(num)}\n'
      f'O triplo de {num} é {triplo(num)}')
