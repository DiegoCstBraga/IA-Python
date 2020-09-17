w = [0.22, -0.33,0.44]

x1 = ([-1,-1],
    [0.1, 0.1],
    [0.1,0.5],
    [0.3, 0.3])

x2 = ([-1,-1],
    [0.6, 0.6],
    [0.8,0.2],
    [0.9, 0.5])

funcAtivacao, limiar, u0 = 0.0, 0.0, 0.0
f, y2, y1 = 0, 1, 0
taxaAprendizado = 0.1

def interacaoPerceptron():
    n = 0

    while n < 10:
        for v in range(1, 4):
            w = entradaX1(w,v)
            w = entradaX2(w,v)
    
    n += 1
    print(f"Numero de treinamentos: {n}\n")

# Codigo Helmuth

def entradaX1 (w, u):
    w, u = [], 0
    print("Entrada  X1\n")
    u0 = 0

    u0 = w[0]*x1[0][0] + w[1]*x1[u][0] + w[2]*x1[u][1]
    print(f"u0 = {u0}")

    if u0 > limiar:
        f = 1
    else:
        f = 0

    print(f"valor de f = \t {f}")

    w[0]=w[0]+taxaAprendizado*(y1-f)*x1[0][0]
    print("Pesos w =\t{w[0]}")
    w[1]=w[1]+taxaAprendizado*(y1-f)*x1[u][0]
    print("Pesos w =\t{w[1]}")
    w[2]=w[2]+taxaAprendizado*(y1-f)*x1[u][1]
    print("Pesos w =\t{w[2]}")

    return w 

# Codigo Diego

def entradaX2 (w, u):
    w, u = [], 0
    print("Entrada X2\n")

    u0 = 0
    u0 = w[0] * x2[0][0] + w[1]*x2[u][0]+w[2]*x2[u][1]
    print(f"u0 = {u0}")

    if u0 > limiar:
        f = 1
    else:
        f = 0
    
    print(f"Valor de f =\t{f}")

    w[0]=w[0]+taxaAprendizado*(y2-f)*x2[0][0]
    print("Pesos w =\t{w[0]}")
    w[1]=w[1]+taxaAprendizado*(y2-f)*x2[u][0]
    print("Pesos w =\t{w[1]}")
    w[2]=w[1]+taxaAprendizado*(y2-f)*x2[u][1]
    print("Pesos w =\t{w[2]}")

    return w

# Codigo Loan

def verificaPerceptron(self, w, x1, x2):
    print("Teste da rede neural \n")
    self.w = w
    for i in w.length:
        print("Pesos resultante do treinamento")
        print("w[" + i + "] = " + w[i])
    
    u0 = 0

    for p in range(1, 4):
        u0 = w[0]*x1[0][0] + w[1]*x1[p][0] + w[2]*x1[p][1]
        print("u0 = " + u0)

    if u0 > limiar:
        f = 1
    else:
        f = 0

    print("teste da entrada x1 saida y = " + f)


    u0 = 0

    for p in range(1, 4):
        u0 = w[0]*x2[0][0] + w[1]*x2[p][0] + w[2]*x2[p][1]
        print("u0 = " + u0)

    if u0 > limiar:
        f = 1
    else:
        f = 0

    print("teste da entrada x2 saida y = " + f)

        
x3 = ([-1,-1],
    [0.0, 0.0],
    [0.15,0.2],
    [0.33, 0.1])

x4 = ([-1,-1],
    [0.77, 0.55],
    [0.8,0.1],
    [0.95, 0.75])

interacaoPerceptron()
verificaPerceptron(w, x3, x4)