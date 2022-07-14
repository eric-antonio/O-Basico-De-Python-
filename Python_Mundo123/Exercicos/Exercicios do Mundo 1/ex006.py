#Crie um algoritimo que leia um numero e mostre o seu dobro triplo e a sua raiz quadrada
n1=int(input('Insira um numero : '))
print('O numero inserido foi : {}\n O dobro é : {} \n O seu triplo é : {} \n A sua raiz quadrada é :{:.2}'.format(n1,n1*2,n1*3,pow(n1,(1/2))))