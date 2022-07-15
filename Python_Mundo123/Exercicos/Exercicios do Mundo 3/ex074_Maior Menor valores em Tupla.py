from random import randint
# Na linha a baixo temos um valor randomizado que foi adicionado a uma varivael!
# gerrador = randint(0,5) 
# Agora se pretendemos gerar uma tupla com valores gerandos de forma randomica, 
# Podemos fazer o seguinte:
# Para cada espaço na Tupla gerar um unico valor Rand
# Explempo: tupla = (randint(1,10),....)
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'\033[1;34m Os valores sorteados foram: \033[m',  end='')

for i in tupla:
    print(f' {i} ' , end= '')
#Para a linguagem Python é possivel achar o maior com as funções max() e min()
print(f'\n O maior valor encontrado foi: {max(tupla)}')
print(f'O menor valor encontrado foi: {min(tupla)}')