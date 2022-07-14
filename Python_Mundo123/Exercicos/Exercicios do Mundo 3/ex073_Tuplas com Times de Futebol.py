equipes = ('Real Madrid', 'Barcelona', 'Atlético Madrid', 'Sevilla', 'Real Betis',
           'Real Sociedad', 'Villarreal', 'Athletic Club', 'Valencia', 'Osasuna',
           'Celta de Vigo', 'Elche', 'Rayo Vallecano', 'Espanyol', 'Getafe', 'Mallorca',
           'Cádiz', 'Granada' , 'Levante', 'Deportivo Alavés')

print(f'Lista Actual da Laliga')
cont=1
print(f'\033[0;34m =========== Lista Actual da Laliga =============\033[m')
for t in  equipes:
    print(f'\033[0;33m {cont} Lugar: \033[m \033[0;32m  {t}\033[m ')
    cont += 1

print(f'\033[0;35m =========== Lista Actual dos 5 Primeiros colocados =============\033[m')
print(f'\033[1;36m {equipes[0:5]}\033[m')


print(f'\033[0;31m =========== Lista Actual dos 4 Ultimos colocados =============\033[m')
#print(f'\033[1;36m {equipes[16:20]}\033[m') ou
print(f'\033[1;36m {equipes[-4:]}\033[m')


print(f'\033[0;35m =========== Lista em ordem Alfabetica =============\033[m')
print(f'\033[1;36m {sorted(equipes)}\033[m')

print(f'\033[0;35m =========== Equipe na 8 Posição =============\033[m')
print(equipes.index('Real Madrid'))