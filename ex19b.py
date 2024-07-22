# Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos 
# alunos e escrevendo na tela o nome do escolhido.
# ex03


from random import choice

# Solicita os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Cria uma lista com os nomes dos alunos
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteia um aluno aleatoriamente
aluno_escolhido = choice(alunos)

# Exibe o nome do aluno escolhido
print(f"O aluno escolhido para apagar o quadro é: {aluno_escolhido}")