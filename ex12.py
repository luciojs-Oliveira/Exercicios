# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5 % de desconto.

prod = float(input('Digite o valor do produto R$ : '))
novo_pre =  prod - (5/100 * prod) 
print(f'O preço do produto de R$ {prod:.2f} com desconto de 5% será de R$ {novo_pre:.2f}')
