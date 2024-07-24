# Crie um programa que leia o nome de um cidade e diga se ela começa ou não com o nome "SANTO".

cid = str(input('Digite a cidade onde você nasceu ? ')).strip()
print(cid[:5].upper() == "SANTO")

