# Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.
print('-' * 40)
metros = float(input("Digite uma distância em metro(s): "))
print('-' * 40)
centimetros = metros * 100
milímetros = metros * 1000

print(f"{metros:.1f} metro(s) equivalem a {centimetros:.0f} centímetros.")
print('-' * 40)
print(f"{metros:.1f} metro(s) equivalem a {milímetros:.0f} milímetros.")
print('-' * 40)
