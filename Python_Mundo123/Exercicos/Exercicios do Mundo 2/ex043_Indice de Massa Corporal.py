peso = float(input('\033[0;33m Qual é o seu pesso?(kg): '))
altura = float(input(' Qual é a sua altura?(m): \033[m'))
imc = peso / (altura ** 2)
print('\033[0;35m O IMC dessa pessoa é de {:.2f} \033[m'.format(imc), end='')

if imc < 18.5:
    print('\033[0;31m Você está Abaixo do peso Normal')
elif 18.5 <= imc < 25:
    print('\033[0;34m Você esta com o Pesso Ideal')
elif 25 <= imc <30:
    print('\033[0;35m Você esta em Sobrepeso')
elif 30 <= imc <40:
    print('\033[0;33m Você esta em Obesidade')
elif imc >= 40:
    print('\033[0;31m Você esta em Obesidade Mórbida')
