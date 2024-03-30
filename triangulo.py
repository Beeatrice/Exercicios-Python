# -*- coding: utf-8 -*-
# Programa: triangulo.py
# Programador: Beatriz Sanabria 
# Data: 28/03/2024
# Este programa lê três números reais e verifica se eles
# podem ser os comprimentos dos lados de um triângulo e se forem,
# verificar se é um triângulo equilátero, isósceles ou escaleno. Se não
# formarem um triangulo, escrevem uma mensagem.
# início do módulo principal
# descrição das variáveis utilizadas
# float lado1, lado2, lado3
# bool triângulo
# str msg

a = float(input())
b = float(input())
c = float(input())

# Passo 2. Verifique se os números formam um triângulo
if a < b + c and b < a + c and c < a + b:
    # Passo 3. Determine o tipo de triângulo
    if a == b == c:
        tipo = 'equilátero'
    elif a == b or a == c or b == c:
        tipo = 'isósceles'
    else:
        tipo = 'escaleno'
    
    # Passo 4. Imprima os lados e o tipo de triângulo
    print(f'lados: {a:.2f}, {b:.2f}, {c:.2f} - {tipo}')
else:
    # Passo 5. Caso não seja um triângulo, imprima a mensagem adequada
    print(f'lados: {a:.2f}, {b:.2f}, {c:.2f} - não é triângulo')
