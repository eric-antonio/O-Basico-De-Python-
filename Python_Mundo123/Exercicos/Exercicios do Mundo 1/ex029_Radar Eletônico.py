from time import sleep

#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapsar 80km/h mostre uma mensagem que ele foi multado.
# A multa vai custar 7,00 por cada Km acima do limite.

velocidade=float(input('Insira a volociadade de um carro: '))
if velocidade >80:
    print('.......Processando a sua velocidade......')
    sleep(3)
    print('Multado! você excedeu o limite permitido que é de 80km/h')
    multa=(velocidade-80)*7
    print('Você deve pagar uma multa de {:.2f}Mzn'.format(multa))
else:
    print('.......Processando a sua velocidade......')
    sleep(3)
    print('Tenha um bom dia e dirija com Segurança')