'''
Programa: Import_Random_Escolha_aleatoria.py
Programadora: Beatriz Sanabria
Data: 01/06/2023

Faça um programa de acordo com o problema:
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles escrevendo o nome do escolhido.
'''
# import random random.choice ele escolhe aleatoriamente

import random
aluno1 = str(input('1° Aluno: '))
aluno2 = str(input('2° Aluno: '))
aluno3 = str(input('3° Aluno: '))
aluno4 = str(input('4° Aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

