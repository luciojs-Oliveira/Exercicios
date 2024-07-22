# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o valor so salário do funcionário R$ : '))
novo_salario = salario + (salario * 15/100)

print(f'O salário de R$ {salario} com reajuste será de {novo_salario}')