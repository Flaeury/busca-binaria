import time
from random import randint

# Inicia tempo de execução.
inicio_execucao = time.time()

# Vetor.
vetor = sorted([randint(1, 10000) for _ in range(500000)])


# Valor que será buscado
x = 0

# Inicia a busca com os parâmetros vetor, lado esquerdo, lado direito e valor buscado
# Neste caso, vetor será o vetor, esquerda será 0, direita o tamanho do vetor e x o valor buscado (variável x)


def busca_recursiva(vetor, esquerda, direita, x):

    # Aqui ele compara ambos
    if direita >= esquerda:

        # Escolhe o valor do meio
        mid = esquerda + (direita - esquerda) // 2

        # Se o valor do meio for o mesmo que x, retorna o valor
        if vetor[mid] == x:
            return mid

        # Se o valor do meio for maior que x, significa que o valor buscado está à esquerda.
        elif vetor[mid] > x:

            # Chama denovo a função, os valores de esquerda ficam iguais, mas a direita será o valor do meio -1,
            # pois o antigo meio é descartado logo no "if vetor[mid] == x"
            return busca_recursiva(vetor, esquerda, mid-1, x)

        # Caso o valor do meio for menor que x, significa que o valor buscado está à direita.
        else:
            # Chama denovo a função, os valores de esquerda mudam porque não pode mais ser 0 e sim "mid+1",
            # pois o meio já foi descartado. O valor da direita continua igual.
            return busca_recursiva(vetor, mid + 1, direita, x)

    # Caso ele encontre que a direita já não é maior ou igual a esquerda. Significa que o valor não está ali.
    else:
        return -1


# Inicia a função e informa os valores dos parametros.
posicao_valor_buscado = busca_recursiva(vetor, 0, len(vetor)-1, x)


print("\n")

print("--BUSCA BINÁRIA RECURSIVA DO VETOR 1--")

# Quando o valor for encontrado
# if posicao_valor_buscado != -1:
#     print(f"Elemento encontrado na posição {posicao_valor_buscado}.")

# # No caso de ser -1, ou seja, não haver o valor.
# else:
#     print("Elemento não encontrado no vetor.")

fim_execucao = time.time()
tempo_execucao = fim_execucao - inicio_execucao

# print(f"Tempo de execução foi: {tempo_execucao:.10f} segundos.")
