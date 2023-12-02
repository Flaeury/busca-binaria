import busca_iterativa.iterativo as iterativo1
import busca_iterativa.iterativo2 as iterativo2
import busca_iterativa.iterativo3 as iterativo3

import busca_recursiva.recursivo as recursivo1
import busca_recursiva.recursivo2 as recursivo2
import busca_recursiva.recursivo3 as recursivo3

import matplotlib.pyplot as plt


tempo0000 = iterativo1.tempo_execucao
tempo0001 = iterativo1.tempo_execucao
tempo0010 = iterativo1.tempo_execucao
tempo_iterativo1 = (tempo0000 + tempo0001 + tempo0010) / 3

tempo0011 = iterativo2.tempo_execucao
tempo0100 = iterativo2.tempo_execucao
tempo0101 = iterativo2.tempo_execucao
tempo_iterativo2 = (tempo0011 + tempo0100 + tempo0101) / 3

tempo0110 = iterativo3.tempo_execucao
tempo0111 = iterativo3.tempo_execucao
tempo0002 = iterativo3.tempo_execucao
tempo_iterativo3 = (tempo0110 + tempo0111 + tempo0002) / 3


tempo1000 = recursivo1.tempo_execucao
tempo1001 = recursivo1.tempo_execucao
tempo1010 = recursivo1.tempo_execucao
tempo_recursivo1 = (tempo1000 + tempo1001 + tempo1010) / 3

tempo1011 = recursivo2.tempo_execucao
tempo1100 = recursivo2.tempo_execucao
tempo1101 = recursivo2.tempo_execucao
tempo_recursivo2 = (tempo1011 + tempo1100 + tempo1101) / 3

tempo1110 = recursivo3.tempo_execucao
tempo1111 = recursivo3.tempo_execucao
tempo1002 = recursivo3.tempo_execucao
tempo_recursivo3 = (tempo1110 + tempo1111 + tempo1002) / 3


def plotar_grafico(tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3):
    codigos_iterativos = ['Iterativo1', 'Iterativo2', 'Iterativo3']
    codigos_recursivos = ['Recursivo1', 'Recursivo2', 'Recursivo3']

    plt.plot(codigos_iterativos, [
             tempo_iterativo1, tempo_iterativo2, tempo_iterativo3], label='Iterativo', marker='o')
    plt.plot(codigos_recursivos, [
             tempo_recursivo1, tempo_recursivo2, tempo_recursivo3], label='Recursivo', marker='x')

    plt.title('Tempo de Execução de Busca Binária Recursiva e Iterativa')
    plt.xlabel('Código')
    plt.ylabel('Tempo de Execução (s)')
    plt.legend()
    plt.show()


def tempo():
    tempo_iterativo1 = iterativo1.tempo_execucao
    tempo_iterativo2 = iterativo2.tempo_execucao
    tempo_iterativo3 = iterativo3.tempo_execucao

    tempo_recursivo1 = recursivo1.tempo_execucao
    tempo_recursivo2 = recursivo2.tempo_execucao
    tempo_recursivo3 = recursivo3.tempo_execucao

    plotar_grafico(tempo_iterativo1, tempo_iterativo2, tempo_iterativo3,
                   tempo_recursivo1, tempo_recursivo2, tempo_recursivo3)


tempo()
