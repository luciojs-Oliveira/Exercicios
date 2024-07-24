# Faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o último nome separadamente.


n = str(input('Digite um frase : ')).strip()
frase = n.split()


print(f'O seu primeita nome é : {frase[0]}')
print(f'O seu último nome é : {frase[len(frase)-1]}')

