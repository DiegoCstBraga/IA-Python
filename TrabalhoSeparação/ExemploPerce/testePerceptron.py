from Perce import interacaoPerceptron, verificaPerceptron

x3 = ([-1, -1], [0.0, 0.0], [0.15, 0.2], [0.33, 0.1])

x4 = ([-1, -1], [0.77, 0.55], [0.8, 0.1], [0.95, 0.75])

w = [0.22, -0.33, 0.44]

interacaoPerceptron(w)
verificaPerceptron(w, x3, x4)
