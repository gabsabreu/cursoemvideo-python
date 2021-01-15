#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = int(input('Quantos reais você tem na carteira? R$'))
#considerando US$ 1,00 = R$3,27
d = r / 3.27
print('Você pode comprar US${:.2f}'.format(d))