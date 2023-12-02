import time

# Inicia tempo de execução.
inicio_execucao = time.time()

# Vetor.
vetor = [5, 6, 7, 10, 12, 15, 15, 16, 18, 18, 21, 23, 26, 28, 32, 33, 33, 33, 35, 38, 38, 38, 39, 41, 42, 43, 45, 47, 48, 48, 51, 52, 54, 56, 57, 62, 66, 67, 68, 69, 70, 70, 73, 73, 73, 79, 81, 85, 87, 87, 88, 89, 91, 101, 104,
         106, 107, 107, 108, 109, 112, 116, 118, 123, 131, 131, 131, 132, 133, 133, 133, 138, 142, 144, 147, 148, 148, 149, 149, 149, 153, 153, 154, 155, 163, 165, 167, 169, 171, 172, 173, 173, 185, 185, 189, 190, 191, 192, 195, 198]

# Ordena o vetor
vetor.sort()

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

print("--BUSCA BINÁRIA RECURSIVA DO VETOR 3--")

# Quando o valor for encontrado
# if posicao_valor_buscado != -1:
#     print(f"Elemento encontrado na posição {posicao_valor_buscado}.")

# # No caso de ser -1, ou seja, não haver o valor.
# else:
#     print("Elemento não encontrado no vetor.")

fim_execucao = time.time()
tempo_execucao = fim_execucao - inicio_execucao

# print(f"Tempo de execução foi: {tempo_execucao:.10f} segundos.")
