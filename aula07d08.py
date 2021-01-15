#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = int(input('Digite o valor em metros para conversão: '))
cm = m * 100
mm = m * 1000
print('centimetros {} milimetros {}'.format(cm,mm))