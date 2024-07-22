# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos aluno.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

# Solicita os nomes dos quatro alunos
n1 = input("Digite o nome do primeiro aluno: ")
n2 = input("Digite o nome do segundo aluno: ")
n3 = input("Digite o nome do terceiro aluno: ")
n4 = input("Digite o nome do quarto aluno: ")

# Cria uma lista com os nomes dos alunos
lista = [n1, n2, n3, n4]

# Embaralha a lista
shuffle(lista)

# Exibe a ordem de apresentação
print("A ordem de apresentação será:")
for nome in lista:
    print(nome)
