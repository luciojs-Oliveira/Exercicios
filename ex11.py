# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessária para pintá - la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados. 



larg = float(input('Digite a largura a ser calculada : '))
altura = float(input('Digite a altura a ser calculada : '))

area = larg * altura

print(f'Analisando a altura de {larg:.2f} m² x {altura:.2f} m² largura a area aser pintada é {area:.2f}m²')

tinta = area / 2

print(f'Você precisa de {tinta} litros para pintar uma area de {area} m²')
