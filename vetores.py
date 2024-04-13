#Programadora: Beatriz Sanbria
#Projete e implemente um programa para ler dois vetores a⃗ e b⃗, representados por duas listas, calcular a soma c⃗ =a⃗ +b⃗ das duas listas e imprimir o resultado c⃗ 


Considerando que os vetores têm n elementos cada, representados pelas listas a e b, tem a soma representada pela lista c dada por:
# Ler as listas de entrada
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Inicializar a lista para armazenar a soma
c = []

# Calcular a soma das listas a e b
for i in range(len(a)):
    c.append(a[i] + b[i])

# Imprimir a lista resultante
print(c)
