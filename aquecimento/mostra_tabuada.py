''' Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, 
 de acordo com a escolha da pessoa usuária. 
 Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:
 Tabuada do 7:
 7 x 0 = 0
 7 x 1 = 7
 [...]
 7 x 10 = 70'''

# Requisitando o número
num = int(input("Digite um número inteiro de 1 a 10:"))

# Gerando a função tabuada()
def tabuada(numero: int):
  print(f'Tabuada do {numero}:')
  for i in range(11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')

# lendo a tabuada do número escolhido
tabuada(num)
