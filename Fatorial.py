#-*- coding: utf-8 -*-
#Programa: Fatorial.py
#Programadora: Beatriz Sanabria
#Data: 25/04/2023


n = int(input())

fatorial = 1
for i in range(1, n+1):
    fatorial *= i

print(fatorial)
