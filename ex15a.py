# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite quantos dias você ficou com o carro: "))

preco_por_dia = 60
preco_por_km = 0.15

preco_a_pagar = km * preco_por_km + dias * preco_por_dia

print(f"Total a pagar: R$ {preco_a_pagar:.2f}")