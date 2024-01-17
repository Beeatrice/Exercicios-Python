#Inserindo vários itens na lista
#Outra forma de criar uma lista é utilizando o while + input, então até que a informação da caixa de entrada seja vazia o programa irá armazenar as informações em uma lista.

while atividade:
   atividade = input('Insira uma atividade: ')
   tarefas.append(atividade)
#Insira uma atividade: Me inscrever no canal da Hashtag
#Insira uma atividade: Fazer o download do minicurso de Python
#Insira uma atividade: Compartilhar o vídeo da Hashtag
#Insira uma atividade
#A estrutura abaixo indica que pegará os itens da posição [0] até o penúltimo item da lista [-2]:

print(tarefas[:-2])
['Curtir o video de listas da Hashtag', 'Me inscrever no canal da Hashtag', 'Fazer o download do minicurso de Python']
#Já no exemplo a seguir temos a utilização da estrutura FOR para percorrer todos os elementos e fazer o print de cada um deles.

for tarefa in tarefas:
   print(tarefa)
#Curtir o video de listas da Hashtag
#Me inscrever no canal da Hashtag
#Fazer o download do minicurso de Python
#Compartilhar o vídeo da Hashtag
