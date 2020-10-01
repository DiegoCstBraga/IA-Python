x1 = ([0.2, 0.64], [0.24, 0.68], [0.28, 0.72], [0.32, 0.76])

x2 = ([0.28, 0.64], [0.32, 0.68], [0.36, 0.72], [0.42, 0.76])

funcAtivacao, limiar, u0 = 0.0, 0.0, 0.0
f, classe0, classe1 = 0, 0, 1
taxaAprendizado = 0.12


def interacaoPerceptron(w):
    n = 0

    while n < 10:
        for v in range(1, 4):
            w = entradaX1(w, v)
            w = entradaX2(w, v)
        n = n + 1

      #   print(f"Numero de treinamentos: {n}\n")


def entradaX1(w, u):
    #  print("----------------------------------\n")
    #  print("Entrada X1")
    u0 = 1

    u0 = w[0] * x1[0][0] + w[1] * x1[u][0] + w[2] * x1[u][1]
    #  print("u0 = %s" % {u0})

    if u0 > limiar:
        f = 1
    else:
        f = 0

    w[0] = w[0] + taxaAprendizado * (classe0 - f) * x1[0][0]
    #  print("Pesos w = %s" % {w[0]})
    w[1] = w[1] + taxaAprendizado * (classe0 - f) * x1[u][0]
    #  print("Pesos w = %s" % {w[1]})
    w[2] = w[2] + taxaAprendizado * (classe0 - f) * x1[u][1]
    #  print("Pesos w = %s" % {w[2]})

    return w


def entradaX2(w, u):
    #  print("\nEntrada X2")
    u0 = 0

    u0 = w[0] * x2[0][0] + w[1] * x2[u][0] + w[2] * x2[u][1]
    #  print("u0 = %s" % {u0})

    if u0 > limiar:
        f = 1
    else:
        f = 0

    #  print(f"Valor de f =\t{f}")

    w[0] = w[0] + taxaAprendizado * (classe1 - f) * x2[0][0]
    #  print("Pesos w = %s" % {w[0]})
    w[1] = w[1] + taxaAprendizado * (classe1 - f) * x2[u][0]
    #  print("Pesos w = %s" % {w[1]})
    w[2] = w[2] + taxaAprendizado * (classe1 - f) * x2[u][1]
    #  print("Pesos w = %s" % {w[2]})

    return w


def verificaPerceptron(w, x1, x2):
    print("Teste da rede neural \n")
    for i in range(len(w)):
        print("\nPesos resultante do treinamento")
        print("w[" + str(i) + "] = " + str(w[i]))

    u0 = 1
    for p in range(1, 7):
        u0 = w[0] * x1[0][0] + w[1] * x1[p][0] + w[2] * x1[p][1]
        print("\nu0 = " + str(u0))

        if u0 > limiar:
            f = 1
        else:
            f = 0

        print("Teste da entrada x1 saida y = " + str(f))

    u0 = 0
    for p in range(1, 7):
        u0 = w[0] * x2[0][0] + w[1] * x2[p][0] + w[2] * x2[p][1]
        print("\nu0 = " + str(u0))

        if u0 > limiar:
            f = 1
        else:
            f = 0

        print("Teste da entrada x2 saida y = " + str(f))
