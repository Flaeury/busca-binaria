import busca_iterativa.iterativo as iterativo0
import busca_iterativa.iterativo1 as iterativo1
import busca_iterativa.iterativo2 as iterativo2
import busca_iterativa.iterativo3 as iterativo3
import busca_iterativa.iterativo4 as iterativo4

import busca_recursiva.recursivo as recursivo0
import busca_recursiva.recursivo1 as recursivo1
import busca_recursiva.recursivo2 as recursivo2
import busca_recursiva.recursivo3 as recursivo3
import busca_recursiva.recursivo4 as recursivo4

import matplotlib.pyplot as plt


def plotar_grafico(tempo_iterativo0, tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_iterativo4, tempo_recursivo0, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3, tempo_recursivo4):
    codigos_iterativos = ['1000',
                          '10000', '100000', '1000000', '5000000']
    codigos_recursivos = ['1000',
                          '10000', '100000', '1000000', '5000000']

    plt.plot(codigos_iterativos, [
             tempo_iterativo0, tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_iterativo4], label='Iterativo', marker='o')
    plt.plot(codigos_recursivos, [
             tempo_recursivo0, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3, tempo_recursivo4], label='Recursivo', marker='x')

    plt.title('Tempo de Execução de Busca Binária Recursiva e Iterativa')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Tempo de Execução (s)')
    plt.legend()
    plt.show()


def tempo():
    tempo_iterativo0 = iterativo0.tempo_execucao
    tempo_iterativo1 = iterativo1.tempo_execucao
    tempo_iterativo2 = iterativo2.tempo_execucao
    tempo_iterativo3 = iterativo3.tempo_execucao
    tempo_iterativo4 = iterativo4.tempo_execucao
    tempo_recursivo0 = recursivo0.tempo_execucao
    tempo_recursivo1 = recursivo1.tempo_execucao
    tempo_recursivo2 = recursivo2.tempo_execucao
    tempo_recursivo3 = recursivo3.tempo_execucao
    tempo_recursivo4 = recursivo4.tempo_execucao

    plotar_grafico(tempo_iterativo0,  tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_iterativo4,
                   tempo_recursivo0, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3, tempo_recursivo4)


tempo()
