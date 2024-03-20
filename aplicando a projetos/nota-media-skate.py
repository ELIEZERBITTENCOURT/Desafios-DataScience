''' Você foi contratado(a) como cientista de dados de uma associação de skate.
 Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, 
 você precisa criar um código que calcula a pontuação dos(as) atletas. 
 Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
 Para calcular a pontuação de um(a) skatista, 
 você precisa eliminar a maior e a menor pontuação dentre as 5 notas e 
 tirar a média das 3 notas que sobraram.
 Retorne a média para apresentar o texto:
 "Nota da manobra: [media]"
'''
# declarando a lista de notas
notas = []
# laço for para pedir as 5 notas e armazená-las na lista notas
for i in range(1,6):
  nota = float(input(f"Digite a {i}ª nota: "))
  notas.append(nota)

# Função para remover a maior e menor nota e retornar a média das notas restantes
def media(lista):
  lista.remove(max(lista))
  lista.remove(min(lista))
  return sum(lista) / len(lista)

# Chamando a função e imprimindo a nota da(o) skatista
media = media(notas)
print(f"Nota da manobra: {round(media, 1)}") 

