'''
Programa: Soma_Hipotenusa.py
Programadora: Beatriz Sanabria
Data: 01/06/2023

Faça um programa que leia o comprimento do cateto opsto e cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa 
'''

cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
comprimento_hipo = (cateto_oposto ** 2 +  cateto_adjacente**2) ** (1/2) 
print('O comprimento da hipotenusa é {:.2f}'.format(comprimento_hipo))
