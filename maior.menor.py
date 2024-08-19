# -*- coding: utf-8 -*-
# Programa: maiormenor.py
# Programador: Beatriz 
# Data: 19/08/2024
# Este programa lê dois números inteiros, calcula o maior e o
# menor entre os números e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int num1, num2
# int maior, divisor
# Passo 1. Leia dois números inteiros
print('Leia dois inteiro num1 e num2: ')
num1, num2 = map(int, input().split())

# Passo 2. Calcule o maior e o menor entre num1 e num2
maior = max(num1, num2)
menor = min(num1, num2)

# Passo 3. Imprima os resultados
print('Maior = {0:d}'.format(maior))
print('Menor = {0:d}'.format(menor))

# pós: maior == max(num1,num2) and menor == min(num1,num2)
# fim do módulo principal
