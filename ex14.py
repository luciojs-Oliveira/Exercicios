# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Escreva um programa que converta uma temperatura digitando em graus Fahrenheit e converta para graus Celsius.


C = float(input('Entre com a temperatura em graus Celsius: '))
F = C * (9 / 5) + 32
print(f'Valor em Fahrenheit: {F}°F')


F = float(input('Entre com a temperatura em graus Fahrenheit: '))
C = (F - 32) * (5 / 9)
print(f'Valor em Celsius: {C}°C')
