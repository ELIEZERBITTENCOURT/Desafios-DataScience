'''5. Como desafio, você recebeu a tarefa de desenvolver um código que contabiliza as pontuações de estudantes de uma instituição de ensino de acordo com suas respostas num teste. Este código deve ser testado para um exemplo de 3 estudantes com uma lista de listas em que cada lista possui as respostas de 5 questões objetivas de cada estudante. Cada questão vale um ponto e as alternativas possíveis são A, B, C ou D.

Caso alguma alternativa em um dos testes não esteja entre as alternativas possíveis, você deve lançar um ValueError com a mensagem "A alternativa [alternativa] não é uma opção de alternativa válida". O cálculo das 3 notas só será realizado mediante as entradas com as alternativas A, B, C ou D em todos os testes. Se não for lançada a exceção, será exibida uma lista com as notas em cada teste.

Os dados para o teste do código são:

    Gabarito da prova:

gabarito = ['D', 'A', 'B', 'C', 'A']

Abaixo temos 2 listas de listas que você pode usar como teste

    Notas sem exceção:

testes_sem_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'C', 'A'], ['D', 'B', 'A', 'C', 'A']]

    Notas com exceção:

testes_com_ex = [['D', 'A', 'B', 'C', 'A'], ['C', 'A', 'A', 'E', 'A'], ['D', 'B', 'A', 'C', 'A']]

    Dica: Para verificar se uma entrada da lista não está entre as alternativas possíveis, use a estrutura lista[i] not in ['A','B','C','D']. Por exemplo, 1 not in [2,3,4]... Saída: True.
'''
gabarito = ['D', 'A', 'B', 'C', 'A']

# Criando a função que recebe a lista de listas com as notas dos estudantes
def corretor(testes: list):
  pontuacoes = [] # criando a lista que receberá as pontuações caso a exceção não seja lançada
  try:
    for teste in testes:
      nota = 0 # variável que acumula a nota de cada estudante
      for i in range(len(teste)):
        if teste[i] not in ['A', 'B', 'C', 'D']: # Verificamos se temos uma alternativa valida
          raise ValueError(f'A alternativa {teste[i]} não é uma opção de alternativa válida')
        elif teste[i] == gabarito[i]: # Verificamos se as respostas são iguais e adicionamos à nota
          nota += 1
      pontuacoes.append(nota) # adicionamos a nota do(a) estudante na lista de pontuações
  except Exception as e:
    print(e)
  else:
    return pontuacoes # retornando a lista de pontuações se não lançarmos a exceção
