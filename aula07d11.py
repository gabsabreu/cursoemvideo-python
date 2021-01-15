#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².

lp = int(input('Digite a largura da parede em metros: '))
ap = int(input('Digite a altura da parede em metros: '))
m2 = ap*lp
lt = m2 / 2

print('A área é de {}m²'.format(m2))
print('Sera necessário {} litros de tinta para pintar essa área'.format(lt))