# -*- coding: utf-8 -*-
# Programa: bois01.py
# Programador: Beatriz Sanabria
# Data: 12/04/2024
# Este programa lê um conjunto de dados referentes ao número de
# identificação e o peso dos bois em um frigorífico. O número de
# identificação igual a zero é usado com flag para sinalizar o
# final da entrada. O programa calcula a média dos pesos e o
# peso do boi mais gordo e o peso do boi mais magro, e quantos
# bois obtiveram esses pesos.
# início do módulo principal
# Inicialize as variáveis
 
maiorPeso = 0.0
menorPeso = 5000.0
soma = 0.0
numbois = 0
numgordo = 0
nummagro = 0
numeros = []
pesos = []

# Leia o número e o peso do primeiro boi
numero = int(input())
peso = float(input())

# Enquanto numero > 0 faça
while numero > 0:
    # Adicione numero a lista das identificações
    numeros.append(numero)
    # Adicione peso a lista dos pesos
    pesos.append(peso)
    # Conte o número dos bois
    numbois += 1
    # Leia o número do boi
    numero = int(input())
    # Se o número for 0, interrompa o loop
    if numero == 0:
        break
    # Leia o peso do boi
    peso = float(input())

# Calcule o maior e o menor peso e a soma dos pesos
for i in range(numbois):
    # Calcule o maiorPeso e conte o num de bois com maiorPeso
    if pesos[i] > maiorPeso:
        maiorPeso = pesos[i]
        numgordo = 1
    elif pesos[i] == maiorPeso:
        numgordo += 1
    # Calcule o menor peso e conte num de bois com menorPeso
    if pesos[i] < menorPeso:
        menorPeso = pesos[i]
        nummagro = 1
    elif pesos[i] == menorPeso:
        nummagro += 1
    # Some os pesos dos bois
    soma += pesos[i]

# Calcule a média
media = soma / numbois

# Imprima os resultados
print('{0:.2f}'.format(media))
print('{0:.2f} {1}'.format(maiorPeso, numgordo))
print('{0:.2f} {1}'.format(menorPeso, nummagro))

# pós: soma == Soma i em {0..n-1}:peso[i] and media ==
#      soma/numbois and maiorPeso == max{peso[0]..peso[i-1]} and
#      numgordo == Num i em {0..n-1}:peso[i] == maiorPeso and
#      menorPeso == min{peso[0]..peso[i-1]} and
#      nummagro == Num i em {0..n-1}:peso[i] == menorPeso
# fim do módulo principal
