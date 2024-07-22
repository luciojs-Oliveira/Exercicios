# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Escreva um programa que converta uma temperatura digitando em graus Fahrenheit e converta para graus Celsius.

"""
Utilizaremos as fórmulas convencionais para converter temperaturas entre Celsius e Fahrenheit:

Converter de Celsius para Fahrenheit:
T(°F)=T(°C)×59​+32


Converter de Fahrenheit para Celsius:
T(°C)=(T(°F)−32)×95​
"""


# Conversor de Unidades: Graus Celsius e Fahrenheit

def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheit')
    print('2. Converter de Fahrenheit para Celsius')

def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius: '))
    F = C * (9 / 5) + 32
    print(f'Valor em Fahrenheit: {F}°F')

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print(f'Valor em Celsius: {C}°C')

if __name__ == '__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')
    if escolha == '1':
        cel_fahr()
    elif escolha == '2':
        fahr_cel()