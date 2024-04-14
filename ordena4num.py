# Programa: ordena4num.py
# Este programa lê uma lista de quatro números inteiros, ordena os
# números em ordem não decrescente e imprime a lista ordenada.
# início do módulo principal
# descrição das variáveis utilizadas
# float num1, num2, num3, num4, aux
# bool troca

# pré: num1, num2, num3, num4
num1,num2,num3,num4 = map(float,input().split())
troca = true
while troca:
   troca = false
   if num1 > num2:
      troca = true
      aux = num1
      num1 = num2 # num2 para num1
      num2 = aux # num1 para lista2
   if num2 > num3:
      troca = true
      aux = num2
      num2 = num3 # num3 para num2
      num3 = aux # num2 para num3
   if num3 > num4:
      troca = true
      aux = num3
      num3 = num4 # num4 para num3
      num4 = aux # num3 para num2
print(num1, num2, num3, num4)
