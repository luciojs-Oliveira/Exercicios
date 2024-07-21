# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.


num = int(input('Digite um número para ver a sua tabuada : '))

for c in range(10):
    print(f'{num} x {c} = {num * c}')

