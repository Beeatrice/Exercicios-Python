num = input('Digite 4 numeros de 0 a 9999:')
soma = '000' + num
print(f"Unidade {soma[-1]}")
print(f"Dezena {soma[-2]}")
print(f"Centena {soma[-3]}")
print(f"Milhar {soma[-4]}")

#Pesquisei um pouco e descobri que se você coloca o numero de uma lista como [-1],  
#a contagem por assim dizer, ocorre de trás pra frente
#Ex: N = 1234
#colocando N[-1] pegaria o 4 e assim N[-2] pegaria o 3
#Colando o '000' no inicio facilita na lista se o numero tiver menos de 4 digitos, 
#já quem com - antes dos números a contagem ocorre de trás pra frente.
#Espero que não tenha ficado mais confuso e que isso ajude alguém.
