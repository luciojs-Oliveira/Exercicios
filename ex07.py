# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.


nota1 = float(input('Digite a primeira nota : '))
nota2 = float(input('Digite a segunda nota : '))

# Atenção a ordem de procedencia.
media = (nota1 + nota2) / 2

print(f'Analisando as notas {nota1} e {nota2} a sua média é : {media}')