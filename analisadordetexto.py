#Analisador de texto
nome = str(input('Digite seu nome:').strip())
print('Seu nome em maiusculo:{}'.format(nome.upper()))
print('Seu nome em minusculo:{}'.format(nome.lower()))
print('Seu nome tem ao total de {} letras'.format(len(nome)- nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
