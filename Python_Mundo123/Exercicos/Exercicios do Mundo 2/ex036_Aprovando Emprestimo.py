from  time import sleep
#Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
#Pergunte o valor da casa, o salario d comprador e em quantas anos ele vai pagar.
# A prestação mensal , não pode exceder 30% do salario ou então o emprestimo sera negado!

print(' \033[0;34m ******* Bem Vindo ao Serviço Mobiliario do Banco NetBanks *******\033[m')
emprstimo = float(input('\033[0;33m Qual é o valor da casa que deseja arecadar?": \033[m'))
salario = float(input('\033[0;33m Qual é o seu salario?:\033[m'))
tempo = int(input('\033[0;33m Em quantos anos deseja efectuar o pagamento?:\033[m'))
prestacao_slarial = salario * 30 / 100
prestacao_mensal =  emprstimo / (tempo * 12)

print('Procesando.....')
sleep(3)
if prestacao_mensal >= prestacao_slarial:

   print('\033[0;31m Infelizmente nao podemos aceitar que compre essa casa! \n'
         'Pois o seu salario é de\033[m '
         '\033[0;32m{}MT\033[m '
         '\033[0;31m e o valor mesal é de \033[m '
         '\033[0;32m{}MT\033[m'
         .format(salario,prestacao_mensal))

else:
	print('\033[0;34m Emprestimo aceite!\033[m \n'
          '\033[0;33m Podera pagar a casa em\033[m'
          '\033[0;32m {}\033[m'
          '\033[0;33m anos em parcelas de \033[m \033[0;32m {}MT\033[m'
          '\033[0;33m Ao mês! \033[m'.format(tempo,prestacao_mensal))