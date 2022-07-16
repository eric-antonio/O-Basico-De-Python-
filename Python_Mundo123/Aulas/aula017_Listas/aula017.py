#As listas são mutaveis diferente das Tuplas
#É possivel adicionar novos objectos e apagar!
#Para adicioanr exitem os metodos:
# -apend(); insert


# Para apagar exitem os metodos :
#del lanche[n] ; lanche.pop(n) ; remove('pizza')

#Para organizr é possivel usar o metodo sort() e para inverter a ordem seria lista.sort(reverse=True)
num = [2,7,4,3,1,0,77]
#print(num)
#num.remove(7)
#num.append(929)
#print(num)

#Formas de inicializar uma lista"
#lista = [] ou lista = list()
valores = list()

valores.append(7)
valores.append(9)
valores.append(5)
valores.append(2)
valores.append(4)
for i in valores:
    print(f'{i}...', end='')

#ou
for i,v in enumerate(valores):
    print(f'Na posição {i} temos o numero {v}')