#Manipular cadeias de texto  
frase = ('Curso em video Python')

# Fatiamento
# C u r s o   e m   v i  d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
frase.upper()
# Transforma as strings em maiusculas

frase.lower()
# Transforma as strings em minusculas

frase.count('o')
# Conta quantas vezes mostra a string "o" na lista

frase.count('O', 0, 13)
# Mostra de 0 a 13 quantas vezes '0' aparece na lista

