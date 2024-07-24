# Crie um que leia o nome completo de uma pessoa e mostre :

# O nome com todas as letras maiúsculas e minúsculas.

# Quantas letras ao todo (sem considerar espaços).

# Quantas letras tem o primeiro nome .

nome = str(input('Digite o seu nome completo : ')).strip() # elimina os espaços antes e depois.

print(f'O seu nome em maiúsculo é : {nome.upper()}')
print(f'O seu nome em minúscula é : {nome.lower()}')
print(f'O seu seu nome tem ao todo {len(nome)} letras') # conta quantas letras tem o nome.
print(f'O seu seu nome tem ao todo {len(nome) - nome.count(' ')} letras') # # conta quantas letras tem o (nome - os espaços).
print(f'O seu primeiro nome tem {nome.find(' ')} letras.')


separa = nome.split()
print(f'Seu primeiro nome é : {separa[0]} e ele tem : {len(separa[0])} letras.')
print(f'Seu Segundo  nome é : {separa[1]} e ele tem : {len(separa[1])} letras.')
print(f'Seu Terceiro nome é : {separa[2]} e ele tem : {len(separa[2])} letras.')
print(f'Seu Quarto   nome é : {separa[3]} e ele tem : {len(separa[3])} letras.')
print(f'Seu Quinto   nome é : {separa[4]} e ele tem : {len(separa[4])} letras.')
print(f'Seu Sexto    nome é : {separa[5]} e ele tem : {len(separa[5])} letras.')