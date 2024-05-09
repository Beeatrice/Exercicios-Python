# Lendo os dados da biblioteca
# Lendo o número de livros
n = int(input())
    
# Criando um dicionário para armazenar os livros e suas informações
biblioteca = {}
for _ in range(n):
    livro, autor, estante = input().strip().split(", ")
    biblioteca[livro] = (autor, estante)

# Lendo os livros para busca
# Lendo o número de livros para busca
m = int(input())
    
# Buscando os livros na biblioteca
for _ in range(m):
    livro = input().strip()
    if livro in biblioteca:
        autor, estante = biblioteca[livro]
        print(f"{autor} {estante}")
    else:
        print(f"{livro} não encontrado")
