# Lendo o número de assinantes
num = int(input())

# Criando a lista telefônica
lista_telefonica = []

# Lendo e armazenando os dados dos assinantes na lista telefônica
for _ in range(num):
    sobrenome, nome, telefone = input().split(', ')
    lista_telefonica.append({'sobrenome': sobrenome, 'nome': nome, 'telefone': telefone})

# Lendo o número de consultas
num_consultas = int(input())

# Realizando as consultas
for _ in range(num_consultas):
    nome, sobrenome = input().split()
    encontrado = False
    for assinante in lista_telefonica:
        if assinante['nome'] == nome and assinante['sobrenome'] == sobrenome:
            print(f"{nome} {sobrenome} {assinante['telefone']}")
            encontrado = True
            break
    if not encontrado:
        print(f"{nome} {sobrenome} não tem telefone")
