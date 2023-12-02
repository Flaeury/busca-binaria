import time

# Inicia tempo de execução.
inicio_execucao = time.time()

# Vetor.
vetor = [2, 3, 4, 7, 6, 8, 20, 18, 23, 30, 1,
         10, 13, 14, 15, 17, 21, 22, 25, 27, 28, 29]
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

print("--BUSCA BINÁRIA ITERATIVA DO VETOR 2--")

# Isso aqui para o caso do valor ter sido encontrado
# if posicao_valor_buscado != -1:
#     print(f"Elemento encontrado na posição {posicao_valor_buscado}.")

# # Quando ocorre o -1, ou seja, o menor valor é maior que o maior, que significa que o valor buscado não existe no vetor
# else:
#     print("Elemento não encontrado no vetor.")

fim_execucao = time.time()
tempo_execucao = fim_execucao - inicio_execucao

# print(f"Tempo de execução foi: {tempo_execucao:.10f} segundos.")
