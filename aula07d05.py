#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

n = int(input('Digite um numero: '))
print('O número que você digitou foi: {}'.format(n))
s = n + 1
print('O número sucessor ao que voce digitou é: {}'.format(s))
a = n - 1
print('O número antecessor ao que você digitou é: {}'.format(a))