# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real_moeda = float(input('Digite um valor em Real ser convertido R$: '))
dolar_moeda = 5.00
conversor = real_moeda / dolar_moeda

print(f'Com R$ {real_moeda:.2f} você pode comprar Us$ {conversor:.2f}')


