# Programa: 1018-Cedula.py LISTA
# Programadora: Beatriz Sanabria
# Data: 11/04/2023

# 1° Passo. Vou armazenar na variavel valor os numeros que o usuario digitou 
valor = int(input())
# 1.2° Passo. Vamos criar uma variavel valor_inicial para guardarmos os primeiros numeros digitados pelo usuario e chama-los no final.
valor_inicial = valor 
# 2° Passo. Vamos dividir nota por 100. Depois pegar o resto da divisão e armazenar na variavel valor manipilada sempre pela ultima vez. Assim sucessivamente com todas as notas.
nota100 = valor // 100
valor = valor % 100

nota50 = valor // 50
valor = valor % 50

nota20 = valor // 20
valor = valor % 20

nota10 = valor // 10
valor = valor % 10

nota5 = valor // 5
valor = valor % 5

nota2 = valor // 2
valor = valor % 2

nota1 = valor // 1
valor = valor % 1
# 3° Passo vamos retornar uma lista de notas de troco para o valor que o usuario digitou.
print(valor_inicial)
print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota5))
print("{} nota(s) de R$ 2,00".format(nota2))
print("{} nota(s) de R$ 1,00".format(nota1))
# Fim.
