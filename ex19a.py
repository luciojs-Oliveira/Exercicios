# Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos 
# alunos e escrevendo na tela o nome do escolhido.
# ex02

from random import choice

aluno1 = str(input('Digite o nome do aluno : '))
aluno2 = str(input('Digite o nome do aluno : '))
aluno3 = str(input('Digite o nome do aluno : '))
aluno4 = str(input('Digite o nome do aluno : '))

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido}')

