from math import  sin,cos,tan,radians
#Faça um programa que leia um angulo qualquer
# e retorne o seu sen cos tang .

ang=float(input('Ínsira um angulo :'))
seno=sin(radians(ang))
print('O angolo de {}º o Seno é: {:.2f}'.format(ang,seno))
coseno=cos(radians(ang))
print('O angulo de {}º o Coseno é {:.2f}'.format(ang,coseno))
tangente=tan(radians(ang))
print('O angulo de {}º a Tangente é {:.2f}'.format(ang,tangente))
