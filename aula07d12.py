#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
po = int(input('Digite o preço original: R$'))
pd = po - (po*5/100)
print('O preço do produto com 5% de desconto é R${:.2f}'.format(pd))