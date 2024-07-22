# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

palavra = str(input('Digite uma palavra : '))
print(type(palavra))

# O método lower() é usado para converter todos os caracteres maiúsculos em uma string para caracteres minúsculos.
print(f'A palavra {palavra} escrita em Minuscula é : {palavra.lower()}')

# O método islower() retorna True se todos os caracteres em uma string estiverem em minúsculas, caso contrário, retorna False.
print(f'A palavra {palavra} escrita em Maiscula é : {palavra.islower()}')


# O método upper() é usado para transformar todos os caracteres de uma string em maiúsculas.
print(f'A palavra {palavra} escrita em Maiscula é : {palavra.upper()}')

# O método isupper() verifica se todos os caracteres de uma string estão em maiúsculas.
print(f'A palavra {palavra} escrita em Maiscula é : {palavra.isupper()}')


#  O método isspace() em Python é usado para verificar se uma string contém apenas espaços em branco.
#  Ele retorna True se todos os caracteres da string forem espaços em branco (como espaços, tabulações ou quebras de linha),
#  e False se a string contiver pelo menos um caractere que não seja espaço em branco
print(f'A palavra {palavra} escrita em Maiscula é : {palavra.isspace()}')

# O método istitle() em Python é usado para verificar se uma string tem um formato de título.
#  Uma string é considerada em formato de título se todas as palavras na string começarem com uma letra maiúscula
#  e o restante das letras forem minúsculas12345. Por exemplo:
print(f'A palavra {palavra} escrita em Maiscula é : {palavra.istitle()}')

print(f'A palavra {palavra} escrita em Maiscula é : {palavra()}')



