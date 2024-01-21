# Manipulando Strings com metodos 
nome = input('Digite seu nome:')
print("Maiusculas: " + nome.upper()) 

print('Minusculas: ' + nome.lower())

nomeSemEspaco = nome.replace(' ','') #Variavel auxiliar para trocar espaço por nada 
print('Quantidade de letras do seu nome: ' + str(len(nomeSemEspaco))) # Printar a quantidade de caractere da lista de strigs lendo ela sem espaço 

primeiro_nome = nome.split()[0] #Split esta formatando a lista de nome separando ela cada palavra um começo de lista 
print('Quantidade de letra do primeiro nome: ' + str(len(nome.split()[0])))#Split esta contando a quantidade de caractere da primeira posição da lista de palavras
