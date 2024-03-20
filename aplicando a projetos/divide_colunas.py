'''7. Você foi contratado(a) como uma pessoa cientista de dados para auxiliar um laboratório que faz experimentos sobre o comportamento de uma cultura de fungos. O laboratório precisa avaliar constantemente a razão (divisão) entre os dados de pressão e temperatura do ambiente controlado recolhidos durante a experimentação para definir a melhor condição para os testes.

Para cumprir com a demanda, você precisa criar uma função divide_colunas que recebe os dados das colunas de pressão e temperatura (que vem no formato de listas) e gerar uma nova coluna com o resultado da divisão. Os parâmetros da função são as duas listas e você deve tratar dentro dela ao menos 2 tipos de exceções:

    Verificar se as listas têm o mesmo tamanho (ValueError)
    Verificar se existe alguma divisão por zero (ZeroDivisionError)

Para testar a função, vamos realizar a divisão entre duas listas de dados coletados no experimento, com os valores de pressão e temperatura do ambiente controlado.

Como teste, use os seguintes dados:

    Dados sem exceção:

pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

    Dados com exceção:

1) Exceção de ZeroDivisionError

pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

2) Exceção de ValueError

pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

    Dica: Você pode usar zip() para parear os dados da lista_1 com a lista_2. Crie uma estrutura try-except que caso uma das exceções sejam lançadas, podemos ver o tipo de erro na saída.
'''

# criando a função que recebe as duas listas e a operação a ser realizada
def divide_colunas(lista_1: list, lista_2: list) -> list:
  # try-except que verifica se é possível calcular a divisão e lança exceção se as listas tem tamanhos diferentes
  # ou se temos alguma divisão por zero em um dos cálculos entre os números das listas
  try:
    if len(lista_1) != len(lista_2): # Verificando se as listas tem o mesmo tamanho, se não lança uma exceção
      raise ValueError("As listas precisam ter o mesmo tamanho")

    # A função zip pareia os elementos das listas e uma lista é gerada por meio da razão entre os pares
    resultado = [round(a / b, 2) for a, b in zip(lista_1, lista_2)] 
  except ValueError as e:
    print(e)
  except ZeroDivisionError as e:
    print(f"{e}: A 2ª lista não pode possuir um valor igual a 0")
  else:
    return resultado

# Testando no exemplo que não lança exceção
pressoes = [100, 120, 140, 160, 180]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ZeroDivisionError)
pressoes = [60, 120, 140, 160, 180]
temperaturas = [0, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)

# Testando no exemplo que lança exceção (ValueError)
pressoes = [100, 120, 140, 160]
temperaturas = [20, 25, 30, 35, 40]

divide_colunas(pressoes, temperaturas)
