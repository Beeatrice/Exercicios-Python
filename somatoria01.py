# -*- coding: utf-8 -*-
# Programa: somatoria01.py
# Programador: Beatriz 
# Data: 25/04/2024
# Este algoritmo calcula a soma dos n termos sequência
# S = 0/1 + 1/4 + 8/9 + 27/16 + ...
# início do módulo principal
# descrição das variáveis utilizadas
# int num, numerador, denominador
# float termo, soma

# pré: num > 0

num = int(input())
soma = 0.0

# Passo 2. Calcule a soma dos n termos
# Passo 2.1. Compute o primeiro termo
# Passo 2.1.1. Compute o primeiro numerador
numerador = 0
# Passo 2.1.2. Compute primeiro denominador
denominador = 1
# Passo 2.1.3. Compute primeiro termo
termo = numerador / denominador
soma += termo

# Passo 2.2. Para i em [1,num] some os i-ésimos termos
for i in range(1, num):
    # Passo 2.2.1. Some o i-ésimo termo
    numerador = i ** 3
    denominador = (i + 1) ** 2
    termo = numerador / denominador
    soma += termo

# Passo 3. Imprima o valor da soma
print('{0:.6f}'.format(soma))

# pós: soma == Soma i em {1,...,num+1}: termo[i] and
#      termo[i] == (i-1)**3/(i**2)
# fim do módulo principal
