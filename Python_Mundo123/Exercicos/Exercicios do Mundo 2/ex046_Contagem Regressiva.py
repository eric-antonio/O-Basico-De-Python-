from time import sleep

for i in range(10, -1, -1):
    sleep(0.5)
    print('\033[0;35m {}'.format(i))
print('\033[0;36m Parabens Marvolas!!!')