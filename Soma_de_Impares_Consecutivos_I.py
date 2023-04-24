# 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

#Entrada
#O arquivo de entrada contém dois valores inteiros.

#Saída
#O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

# -*- coding: utf-8 -*-
# Programa: Soma_de_Impares_Consecutivos_I.py
# Programadora: Beatriz Sanabria
# Data: 24/04/2023


x = int(input())
y = int(input())

# encontra o menor e o maior valor entre x e y
menor = min(x, y)
maior = max(x, y)

# inicializa a variável soma com zero
soma = 0

# percorre todos os números ímpares entre menor e maior
for num in range(menor+1, maior):
    if num % 2 != 0:
        soma += num

# exibe o valor da soma
print(soma)
