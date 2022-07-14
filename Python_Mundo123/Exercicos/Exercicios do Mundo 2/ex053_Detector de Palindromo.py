frase = str(input('Degite uma frase: ')).strip().upper()
palavars = frase.split()
junto = ''.join(palavars)
inverso = ''

''' 
            Tatica de fatiamento
            inverso = junto[::-1]
            vai pegara a palavra do inicio :
            até ao seu fim :
            de forma regressiva -1
'''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if junto == inverso:
    print('O iverso de  {} é {} logo:'.format(junto,inverso))
    print('\033[33m É um Palindromo')
else:
    print('O iverso de  {} é {} logo:'.format(junto,inverso))
    print('\033[31m Não é um Palindromo')



