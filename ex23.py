# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.


# ex : 01
num = int(input('Informe um número : '))
n = str(num)

print(f'Analisando o número {num}')
print(f'Unidade : {n[3]}')
print(f'Dezena : {n[2]}')
print(f'centena : {n[1]}')
print(f'Milhar : {n[0]}')

