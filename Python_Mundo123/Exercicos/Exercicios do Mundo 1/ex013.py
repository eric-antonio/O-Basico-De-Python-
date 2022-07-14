#Faça um programa que peça o salorio de um fincionario e devolva com 15% de aumento.
salario=float(input('Insira o seu salario:'))
aumento=salario+(salario*15/100)
print('O seu salario são : {:.2f}mt \n O seu aumento foi de: {}% \n Seu novo salario é: {:.2f} mt'.format(salario,15,aumento))