# -*- coding: utf-8 -*-

'''
Programa: Sequência_consecutiva_maior_e_o_número_gerador.py
Programadora: Beatriz Sanabria
Data: 31/05/2023

Deseja-se determinar qual é o tamanho T da maior sequência de números consecutivos de uma lista de inteiros, e qual número N gerou primeiro essa maior sequência. 
'''

# lê a entrada como uma string e separa em uma lista de inteiros
numeros = list(map(int, input().split()))

# inicializa as variáveis de controle da maior sequência
maior_tamanho = 0
num1 = None

# itera sobre cada número da lista
for i in range(len(numeros)):
    tamanho_atual = 1
    # verifica quantos números consecutivos existem depois do número atual
    for j in range(i+1, len(numeros)):
        if numeros[j] == numeros[i]:
            tamanho_atual += 1
        else:
            break
    # se a sequência atual é maior que a maior sequência encontrada até agora, atualiza as variáveis de controle
    if tamanho_atual > maior_tamanho:
        maior_tamanho = tamanho_atual
        num1 = numeros[i]

# imprime o resultado
print('{}: {}'.format(num1, maior_tamanho))
