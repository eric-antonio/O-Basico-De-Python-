#Desenvolva um progtrama que leia um numero inteiro
# qualquer em metros e exiba convertido em centimetros e milimetros

n1=float(input('Insira o valor em metros : '))
dm=n1*10
cm=n1*100
mm=n1*1000
km=n1/1000
hm=n1/100
dam=n1/10
print('O valor inserido é : {}; \nO valor em decimetros é {} \n O valor em centimetros é: {:.0f}cm  ;\n O valor em milimetros é: {:.0f}mm ;'
      '\n O valor em kilometros é {}km \n O valor em hequetometros é {}hm\n O valor em dacametros é {}dam '.format(n1,dm,cm,mm,km,hm,dam))