# -*- coding: utf-8 -*-
# Programa: maiorpalavra01.py
# Programador: Beatreiz
# Data: 19/08/2024
# Este programa le três palavras, computa qual e a maior 
# (lexicograficamente) e imprime a maior.
# início do módulo principal
# descrição das variáveis utilizadas
# string palavra1, palavra2, palavra3, maior

# pré: palavra1 palavra2 palavra3

# Passo 1. Leia as palavras
palavra1 = input().strip()
palavra2 = input().strip()
palavra3 = input().strip()

# Passo 2. Compute a maior palavra
maior = max(palavra1, palavra2, palavra3)

# Passo 3. Imprima a maior palavra		
print('Maior palavra = {0:s}'.format(maior))

# pós: maior and maior == max{palavra1, palavra2, palavra3}
# fim do módulo principal
