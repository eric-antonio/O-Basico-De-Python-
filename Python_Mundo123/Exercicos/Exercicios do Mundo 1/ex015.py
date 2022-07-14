#Escreva um programa que pergunte a quntidade de Km percoridos
# por um carro e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar , sabendo que o carro custa 60mt por dia e 0.15 por Km percorido.
dias=int(input('Quantos dias alugados : '))
km=float(input('Quantos km rodados : '))
pago=dias*60+(km*0.15)
print('O total a pagar é de {:.2f}mt '.format(pago))

