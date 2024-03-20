'''Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
 [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
 Utilize o return na função e salve a nova lista na variável mult_3.
'''
 # Lista gerada
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

# declarando a lista de multiplos de 3 
mult_3 = []
# função para gerar uma lista dos múltiplos de 3 a partir de uma lista
def multiplo_3(lista: list) -> list:
  for i in range(len(lista)):
    # condição para um número ser múltiplo de 3
    if lista[i] % 3 == 0:
      mult_3.append(lista[i])
  return mult_3

# retornando a lista gerada para a variável mult_3
mult_3 = multiplo_3(lista)
mult_3
