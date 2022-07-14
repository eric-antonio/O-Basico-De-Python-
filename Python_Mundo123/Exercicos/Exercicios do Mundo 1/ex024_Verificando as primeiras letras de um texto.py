#Crie um programa que leia o nome de uma
# cidade e diga se ela começa ou nao com o nome "Santo"

cidade=str(input("Insira o nome da Cidade: ")).strip()
print(cidade[0:5].upper() =='SANTO')
