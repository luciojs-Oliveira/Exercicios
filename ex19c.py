# Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos 
# alunos e escrevendo na tela o nome do escolhido.
# ex04


import random

# Lista com os nomes dos alunos
alunos = ["Alice", "Bob", "Carlos", "Diana"]

# Sorteio do aluno
aluno_escolhido = random.choice(alunos)

# Exibição do nome do aluno escolhido
print(f"O aluno escolhido para apagar o quadro é: {aluno_escolhido}")