import matplotlib.pyplot as plt

yIterativa = [0.0027291000001241628,
              0.003913300000021991,
              0.00444389999984196,
              0.005939499999840336,
              0.006530800000291492,
              0.008842500000355358,
              0.009736900000461901,
              0.011082699999860779,
              0.012499500000558328,
              0.01357099999950151,
              0.014019100000041362,
              0.016123599999446014,
              0.01700260000052367,
              0.01865379999981087]

xRecursiva = [10,
              50,
              100,
              500,
              1000,
              5000,
              10000,
              50000,
              100000,
              500000,
              1000000,
              5000000,
              10000000,
              50000000]

yRecursiva = [0.003929099999368191,
              0.005441999999877589,
              0.00630399999954534,
              0.007872900000620575,
              0.008845299999848066,
              0.012591599999723257,
              0.013221799999882933,
              0.015629399999852467,
              0.018283100000189734,
              0.019540400000551017,
              0.021365200000218465,
              0.02323880000039935,
              0.02404859999933251,
              0.02568760000031034]

xIterativa = [10,
              50,
              100,
              500,
              1000,
              5000,
              10000,
              50000,
              100000,
              500000,
              1000000,
              5000000,
              10000000,
              50000000]


def plotar_grafico(xIterativa, yIterativa, xRecursiva, yRecursiva):
    codigos_iterativos = [10, 50, 100, 500, 1000, 5000,
                          10000, 50000, 100000,  500000, 1000000, 5000000, 10000000, 50000000]
    codigos_recursivos = [10, 50, 100, 500, 1000, 5000,
                          10000, 50000, 100000,  500000, 1000000, 5000000, 10000000, 50000000]

    plt.plot(codigos_iterativos, yIterativa, label='Iterativo', marker='o')
    plt.plot(codigos_recursivos, yRecursiva, label='Recursivo', marker='x')

    plt.title('Tempo de Execução de Busca Binária Recursiva e Iterativa')
    plt.xlabel('Tamanho do vetor')
    plt.ylabel('Tempo de Execução (s)')
    plt.legend()
    plt.show()


def tempo():
    plotar_grafico(xIterativa, yIterativa, xRecursiva, yRecursiva)


tempo()
