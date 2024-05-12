# -*- coding: utf-8 -*-
# Programa: somavetores.py
# Programador: Beatriz Sanabria
# Data: 12/05/2024
# Este programa le dois vetores de inteiros e computa imprime a soma
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, soma
# int tam

# Passo 1. Leia e armazene os vetores
a = list(map(float, input().split()))
b = list(map(float, input().split()))

# Passo 2. Calcule a soma dos vetores
soma_vetores = [a + b for a, b in zip(a, b)]

# Passo 3. Imprima a lista representando a soma dos vetores
print(["{:.1f}".format(valor) for valor in soma_vetores])
# pós: soma and para i em {0..tam-1}:soma[i] == a[i]+b[i]
# fim do módulo principal
