#Faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento.
sa = int(input('Digite seu salário atual: R$ '))
sp = sa + (sa*15/100)
print('Seu novo salário com 15% de aumento é R${:.2f}'.format(sp))