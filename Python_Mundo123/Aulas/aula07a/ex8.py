idade= 19%2
print(idade)
n1 = float(input('Insira uma nota: '))
if n1 <= 9:
    print('A nota: {} é Má!'.format(n1))
elif (n1 >= 10) and (n1 <= 13):
    print('A nota: {} é Satisfatoria! '.format(n1))
elif (n1 >= 14 ) and (n1 <= 17):
    print('A nota: {} é Boa!'.format(n1))
elif n1 >= 18:
    print('A nota: {} é Muito Boa!'.format(n1))


