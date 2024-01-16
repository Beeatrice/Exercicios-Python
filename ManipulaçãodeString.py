#Manipular cadeias de texto  
frase = 'Curso em video Python'

# Fatiamento
# C u r s o   e m   v i  d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
frase[1]
# frase[1] vai retornar a string da posição 1 que pedimos!

frase[0:5]
# Frase[0:5] Vai me retornar as strings da posição 0 até a 4!   
# Quando estou mechendo com fatiamento de strings (Range) o ultimo valor não entra na contagem 
# Então [0:5] ele vai pegar a letra que esta na psição 1 até a posição 4!

frase[1:10:2] 
# Aqui o fatiamento acontece da seguinte maneira contamos as strings de 0 a 10 
# Porem de 2 em 2 
# ex: [0 1 - 2 3 - 4 5 - 6 7 - 7 8 - 9 10]
# Tirando sempre o segundo numero contado

frase[:5]
# Aqui vamos fatiar do inicio até a 4 posição da string
# como não informamos o inicia da fatiação, ela pega sozinha do inicio 

frase[15:]
# Aqui o python começa no [15:] e vai até o final!     

frase[0::10]
# Aqui o fatiamento acontece da seguinte maneira contamos as strings de 0 a 10 
# Porem de 3 em 3 
# ex: [0 1 2 - 3 4 5 - 6 7 8 - 9 10]
# Tirando sempre o terceiro numero contado
