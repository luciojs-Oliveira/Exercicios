# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

palavra = str(input('Digite uma palavra : '))
print(type(palavra))
print(f'A palavra {palavra} escrita em Minuscula é : {palavra.lower()}')
print(f'A palavra {palavra} escrita em Maiscula é : {palavra.upper()}')
