#Desenvolva um programa que pergunte a distancia da de uma viagem em KM.
# Calcule o preço da passagem , cobrando 050 por km para viagens
# de ate 200km e 0,45 para viagens mais longas.

distancia=float(input('Qual é a distancia da sua viagem?: '))

if distancia <=200:
    preço=distancia*0.50
    print('O preço da sua viagem é de {:.2f}MT'.format(preço))
else:
    preço = distancia * 0.45
    print('O preço da sua viagem é de {:.2f}MT'.format(preço))
print('Faça uma boa Viagem!')