#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
 # -*- coding: utf-8 -*-
 # Programa: Math.trunc.py
 # Programadora: Beatriz Sanabria
 # Data: 24/04/2023
import math
num = float(input())
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))
