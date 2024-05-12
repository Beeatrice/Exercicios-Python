# -*- coding: utf-8 -*-
# Programa: bois02.py
# Programador:
# Data: 24/02/2016
# Inicialize as variáveis
soma_pesos = 0
bois = []

# Loop para ler os dados dos bois
while True:
    # Leia o número do boi
    numero_boi = int(input())
    if numero_boi == 0:
        break  # Se o número do boi for 0, encerra o loop
    # Leia o peso do boi
    peso_boi = float(input())
    # Adicione o peso à soma total
    soma_pesos += peso_boi
    # Adicione o boi à lista
    bois.append((numero_boi, peso_boi))

# Calcule a média dos pesos
media_pesos = soma_pesos / len(bois)

# Ordene a lista de bois pelo peso
bois.sort(key=lambda x: x[1])

# Imprima a média dos pesos
print(f"Média dos pesos de {len(bois)} bois = {media_pesos:.2f} Kg")

# Imprima os dois bois mais magros
print(f"Boi mais magro 1 = {bois[0][0]} - Peso = {bois[0][1]:.2f} Kg")
print(f"Boi mais magro 2 = {bois[1][0]} - Peso = {bois[1][1]:.2f} Kg")

# Imprima os dois bois mais gordos
print(f"Boi mais gordo 1 = {bois[-1][0]} - Peso = {bois[-1][1]:.2f} Kg")
print(f"Boi mais gordo 2 = {bois[-2][0]} - Peso = {bois[-2][1]:.2f} Kg")
