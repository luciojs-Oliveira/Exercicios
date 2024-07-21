# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá - la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 



larg = float(input('Digite a largura a ser calculada : '))
altura = float(input('Digite a altura a ser calculada : '))

area = larg * altura
tinta = area / 2

print(f"Para pintar uma área de {area:.2f} m², são necessários {tinta:.2f} litros de tinta.")