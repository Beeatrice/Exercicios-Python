# -*- coding: utf-8 -*-

'''
Programa: Inversor_de_letras.py
Programadora: Beatriz Sanabria
Data: 31/05/2023
'''

while True: # O código usa um loop while para ler as entradas até encontrar o fim de arquivo.
    try:
        S = input() # Para cada entrada, é criada uma variável inverted_S que irá armazenar a string invertida.
    except:
        break
    inverted_S = ""
    inversions = 0 # A variável inversions irá armazenar o número de inversões que ocorreram.
    for c in S: # O loop for percorre cada caractere da string S.
        if c.islower():
            inverted_S += c.upper()
        elif c.isupper():
            inverted_S += c.lower()
        else:
            inverted_S += c
        if c.isupper() != inverted_S[-1].isupper():
            inversions += 1
    print(inverted_S + ": " + str(inversions) + " inversões!")


