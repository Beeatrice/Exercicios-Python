lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000,20000,50000]
resultados=[]
Usando range para rodar o for. i é uma variável auxiliar que irá percorrer a posição 0, 1 e 2 da nossas listas. Range(3) indica serem 3 iterações:

for i in range(3):
   tupla=(lojas[i],vendas[i])
   resultados.append(tupla)
print(resultados)
[('Rio de Janeiro', 10000), ('São Paulo', 20000), ('Curitiba', 50000) ]
Para finalizar vamos te mostrar como acessar um item dentro dessa tupla, pois temos um argumento a mais do que temos na lista.

O primeiro é a posição do conjunto e depois será a posição no conjunto, então nesse exemplo temos resultados [1][0].

Isso significa que vamos pegar o conjunto na posição 1 que é referente a São Paulo e 20000. Em seguida pegamos a posição 0 desse conjunto, que corresponde ao nome São Paulo.

Ou seja, primeiro informamos o conjunto que vamos analisar e em seguida qual elemento queremos desse conjunto!

print(resultados[1][0])
São Paulo
Ao fazermos resultados[1][0] acessamos o primeiro item da tupla, ou seja: São Paulo,
