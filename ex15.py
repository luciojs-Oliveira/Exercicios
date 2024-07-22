# Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
#  quais ele foi alugado. Calculae o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 km rodados.

dia = int(input('Digite quantos dias você alugou o carro : '))
km = int(input('Digite quantos quilometros você rodou : '))

diaria =  60
quilometros = 0.15
total = diaria + quilometros

print(f'Valor por diaria {diaria} ')
print(f'Valor por km rodados {quilometros} ')
print(f'O valor total do aluguel é de R$ : {total}')





