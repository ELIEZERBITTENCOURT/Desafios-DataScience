''' Crie uma lista dos quadrados dos números da seguinte lista:
 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
 Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
'''
# Lista dos números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função lambda que eleva um número ao quadrado
quadrado = lambda x: x ** 2

# Utilizando a função map() para aplicar a função lambda em cada número da lista
resultado = list(map(quadrado, numeros))
resultado 
