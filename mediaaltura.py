# -*- coding: utf-8 -*-
# Programa: mediaalturas00.py
# Programador: Beatriz Sanabria
# Data: 12/05/2024
# Este programa lê um conjunto de alturas, conta-as calcula e
# imprime a média, e o número de alturas maiores ou iguais a média.
# A entrada é dada por uma lista de n números reais (alturas), uma
# em cada linha, e a ultima linha contém o número 0.0 que sinaliza
# o final da entrada. Use o append() para ler os elementos da lista.
# A saída consiste em imprimir a média e a quantidade de alturas
# que são maiores ou iguais a média. O valor da média das alturas
# deve ser impresso com duas casas decimais ({0:.2f}).
# início do módulo principal
# descrição das variáveis utilizadas
# Calcule a média das alturas
# list alturas[]
# float media
# int num, tam

# pré: alturas[0]..alturas[tam-1]

# Inicialize a lista de alturas e a variável para a soma das alturas
alturas = []
soma_alturas = 0.0

# Leia as alturas e calcule a soma
while True:
    altura = float(input())
    if altura == 0.0:
        break
    alturas.append(altura)
    soma_alturas += altura

# Calcule a média das alturas
media = soma_alturas / len(alturas)

# Calcule o número de alturas maiores ou iguais à média
num = sum(altura >= media for altura in alturas)

# Imprima a média e o número de alturas maiores ou iguais à média
print("{:.2f}".format(media))
print(num)

# pós: media and num
# fim do módulo principal
