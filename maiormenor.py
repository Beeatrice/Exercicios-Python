# -*- coding: utf-8 -*-
# Programa: maiormenor.py
# Programador: Beatriz Sanabria
# Data: 09/05/2024
# Este programa lê um conjunto de números, calcula o maior, o
# menor número e a variação entre eles e imprime o resultado. 
# O programa usa a função maiormenor para computar o maior, 
# o menor número da lista.

# Esta função recebe uma lista (tamanho e elementos) e computa
# os índices dos elementos máximo e mínimo da lista
def maiormenor(lista):
    tam = len(lista)
    if tam == 0:
        return -1, -1, -1, -1
    
    # Inicializando variáveis para armazenar o índice e o valor do maior e do menor elemento
    indmax = 0
    maximo = lista[0]
    indmin = 0
    minimo = lista[0]

    # Iterando sobre os elementos da lista para encontrar o máximo e o mínimo
    for i in range(1, tam):
        if lista[i] > maximo:
            maximo = lista[i]
            indmax = i
        elif lista[i] < minimo:
            minimo = lista[i]
            indmin = i

    # Imprimindo os resultados
    print('{0:d} {1:d} {2:d} {3:d}'.format(indmax, maximo, indmin, minimo))

# módulo principal
# Passo 1. Leia a lista
# Passo 1.1. Leia o tamanho da lista
entrada = input().split()
tam = len(entrada)

# Passo 1.2. Leia os elementos da lista
lista = list(map(int, entrada))

# Passo 2. Compute o maior e o menor elemento da lista
maiormenor(lista)
# pós: maximo and maximo == max i em {0,...,tam-1}: lista[i]
#      minimo and minimo == min i em {0,...,tam-1}: lista[i]
# fim do módulo principal
