# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite um frase : ')).upper().strip()

print(f'A letra A aparece {frase.count('A')} vezes na frase.')
print(f'A primeita letra A aparece na posiçao {frase.find('A')+1}.')
print(f'A última letra A aparece na posição {frase.rfind('A')+1}.')

