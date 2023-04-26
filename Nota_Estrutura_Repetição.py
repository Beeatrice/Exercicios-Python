#-*- coding: utf-8 -*-
#Programa: Nota_Estrutura_Repetição.py
#Programadora: Beatriz Sanabria
#Data: 25/04/2023

notas_validas = 0
soma_notas = 0

while notas_validas < 2:
    nota = float(input())
    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        soma_notas += nota
        notas_validas += 1

media = soma_notas / 2
print(f"media = {media:.2f}")
