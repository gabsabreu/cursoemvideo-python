#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira

import math
num = float(input('Digite algum numero real: '))
nr = math.floor(num)
print('O numero {} tem a parte inteira {}'.format(num,nr))