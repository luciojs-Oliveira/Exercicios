# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA".

nome = str(input('Digite o seu nome completo : ')).strip()
print(f'Seu nome tem "silva" ? {'silva' in nome.lower()}')

