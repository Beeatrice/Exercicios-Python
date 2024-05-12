# -*- coding: utf-8 -*-
# Programa: semrepeticao.c
# Programador: Beatriz SAnabria
# Data: 12/05/2024
# Este programa lê uma lista de  n itens, retira os elementos
# repetidos da lista e imprime o resultado.
# Passo 1. Leia a lista de números inteiros
from collections import OrderedDict

# Passo 1. Leia a lista de números inteiros
lista = list(map(int, input().split()))

# Passo 2. Crie um OrderedDict para manter a ordem original dos elementos
ord_dict = OrderedDict.fromkeys(lista)

# Passo 3. Converta o OrderedDict de volta para uma lista
lista_sem_duplicatas = list(ord_dict.keys())

# Passo 4. Imprima a lista sem duplicatas
print(lista_sem_duplicatas)
