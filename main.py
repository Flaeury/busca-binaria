import busca_iterativa.iterativo as iterativo0
import busca_iterativa.iterativo1 as iterativo1
import busca_iterativa.iterativo2 as iterativo2
import busca_iterativa.iterativo3 as iterativo3
import busca_iterativa.iterativo4 as iterativo4
import busca_iterativa.iterativo5 as iterativo5
import busca_iterativa.iterativo6 as iterativo6
import busca_iterativa.iterativo7 as iterativo7
import busca_iterativa.iterativo8 as iterativo8
import busca_iterativa.iterativo9 as iterativo9
import busca_recursiva.recursivo as recursivo0
import busca_recursiva.recursivo1 as recursivo1
import busca_recursiva.recursivo2 as recursivo2
import busca_recursiva.recursivo3 as recursivo3
import busca_recursiva.recursivo4 as recursivo4
import busca_recursiva.recursivo5 as recursivo5
import busca_recursiva.recursivo6 as recursivo6
import busca_recursiva.recursivo7 as recursivo7
import busca_recursiva.recursivo8 as recursivo8
import busca_recursiva.recursivo9 as recursivo9

import matplotlib.pyplot as plt


def plotar_grafico(tempo_iterativo0, tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_iterativo4, tempo_iterativo5, tempo_iterativo6, tempo_iterativo7, tempo_iterativo8, tempo_iterativo9, tempo_recursivo0, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3, tempo_recursivo4, tempo_recursivo5, tempo_recursivo6, tempo_recursivo7,  tempo_recursivo8, tempo_recursivo9):
    codigos_iterativos = ['100', '500', '1K', '5K',
                          '10K', '50K', '100K',  '500K', '1M', '5M']
    codigos_recursivos = ['100', '500', '1K', '5K',
                          '10K', '50K', '100K',  '500K', '1M', '5M']

    plt.plot(codigos_iterativos, [
             tempo_iterativo0, tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_iterativo4, tempo_iterativo5, tempo_iterativo6, tempo_iterativo7, tempo_iterativo8, tempo_iterativo9], label='Iterativo', marker='o')
    plt.plot(codigos_recursivos, [
             tempo_recursivo0, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3, tempo_recursivo4, tempo_recursivo5, tempo_recursivo6, tempo_recursivo7, tempo_recursivo8, tempo_recursivo9], label='Recursivo', marker='x')

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
    tempo_iterativo5 = iterativo5.tempo_execucao
    tempo_iterativo6 = iterativo6.tempo_execucao
    tempo_iterativo7 = iterativo7.tempo_execucao
    tempo_iterativo8 = iterativo8.tempo_execucao
    tempo_iterativo9 = iterativo9.tempo_execucao

    tempo_recursivo0 = recursivo0.tempo_execucao
    tempo_recursivo1 = recursivo1.tempo_execucao
    tempo_recursivo2 = recursivo2.tempo_execucao
    tempo_recursivo3 = recursivo3.tempo_execucao
    tempo_recursivo4 = recursivo4.tempo_execucao
    tempo_recursivo5 = recursivo5.tempo_execucao
    tempo_recursivo6 = recursivo6.tempo_execucao
    tempo_recursivo7 = recursivo7.tempo_execucao
    tempo_recursivo8 = recursivo8.tempo_execucao
    tempo_recursivo9 = recursivo9.tempo_execucao

    plotar_grafico(tempo_iterativo0,  tempo_iterativo1, tempo_iterativo2, tempo_iterativo3, tempo_iterativo4, tempo_iterativo5, tempo_iterativo6, tempo_iterativo7, tempo_iterativo8, tempo_iterativo9,
                   tempo_recursivo0, tempo_recursivo1, tempo_recursivo2, tempo_recursivo3, tempo_recursivo4, tempo_recursivo5, tempo_recursivo6, tempo_recursivo7, tempo_recursivo8, tempo_recursivo9)


tempo()
