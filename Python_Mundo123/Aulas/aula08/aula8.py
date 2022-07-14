import random
from math import sqrt, floor
import  emoji

print(emoji.emojize("Ola , Mundo 🌍 ☄ ❤️️",use_aliases=True))

rand=random.randint(1,9)
print('O numero aleatorio é {}'.format(rand))

num=int(input('Insira um numero: '))
raiz=sqrt(num)
print('A raiz do numero {} é {}'.format(num,floor(raiz)))