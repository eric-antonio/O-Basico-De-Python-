from  math import hypot
#Faça um programa que leia o comprimento do cateto adjacente de um triangulo
#retangulo , calcule  e mostre o cumprimento da hipotenusa.
ca=float(input('Insira o cateto Oposto : '))
co=float(input('Insira o cateto Adjacente : '))
hp=hypot(ca,co)
print('O cateto adjacente é {}\n O cateto oposto é {} \n  A sua Hipotenusa é {:.2f} '.format(ca,co,hp))