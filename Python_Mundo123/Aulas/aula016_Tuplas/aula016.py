lanche = ('Milena' , 'Lekyta', 'Suzana', 'Fafá', ' Fernanda')
a = ('1','2' , '4', '5')
b = ('3', '6', '7','8')
c = a + b
print(c)
#tuplas são imutaveis

#Formas de exibir ps dados
#----------1-Forma Simples
#for i in lanche:
#    print(f' Eu vou comer : {i}')

#----------2-Forma Com Range
#for cont in range(0, len(lanche)) :
#    print(f' Eu vou comer : {lanche[cont]}')

#----------3-Forma Com o enumarate
#for i, pessoa in enumerate(lanche):
#    print(f' A Estudante  {pessoa} ' )

# Metodo Sorted- Organiza ou coloca em ordem!
#print(sorted(lanche))