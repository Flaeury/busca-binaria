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

# Inicia a busca com os parâmetros vetor e valor buscado


def busca_iterativa(vetor, x):

    # O menor elemento do vetor
    menor_elemento = 0

    # O maior, subtrai-se 1 devido o primeiro elemento ser visto como 0.
    maior_elemento = len(vetor) - 1

    # Loop while para comparar e ajustar os índices conforme necessário.
    while menor_elemento <= maior_elemento:

        # Valor do meio
        meio = (maior_elemento + menor_elemento) // 2

        # Se o meio é menor que o valor buscado, o menor elemento será o meior + 1, ou seja, descarta tudo aquilo menor que o meio
        if vetor[meio] < x:
            menor_elemento = meio + 1

        # Se o meio é maior que o valor buscado, o maior elemento será o meior + 1, ou seja, descarta tudo aquilo maior que o meio
        elif vetor[meio] > x:
            maior_elemento = meio - 1

        # Para o caso de o meio já ser o valor buscado, que uma horá terá de ser (A não ser que o valor não esteja no vetor)
        else:
            return meio

    return -1


# Aqui o código dará a posição que se encontra o valor buscado no vetor
posicao_valor_buscado = busca_iterativa(vetor, x)


print("\n")

print("--BUSCA BINÁRIA ITERATIVA DO VETOR 3--")

# Isso aqui para o caso do valor ter sido encontrado
# if posicao_valor_buscado != -1:
#     print(f"Elemento encontrado na posição {posicao_valor_buscado}.")

# # Quando ocorre o -1, ou seja, o menor valor é maior que o maior, que significa que o valor buscado não existe no vetor
# else:
#     print("Elemento não encontrado no vetor.")

fim_execucao = time.time()
tempo_execucao = fim_execucao - inicio_execucao

# print(f"Tempo de execução foi: {tempo_execucao:.10f} segundos.")
