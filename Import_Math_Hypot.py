'''
Programa: Import_Math_Soma_Hipotenusa.py
Programadora: Beatriz Sanabria
Data: 01/06/2023

Faça um programa que leia o comprimento do cateto opsto e cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa 
'''
import math
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
comprimento_hipo = math.hypot(cateto_oposto, cateto_adjacente)
print('A hipotenusa vai medir {:.2f}'.format(comprimento_hipo))
