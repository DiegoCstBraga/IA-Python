from Perce import interacaoPerceptron, verificaPerceptron

# Valores usados no treinamento do Perceptron
# x3 = ([-1, -1], [0.28, 0.676], [0.2652, 0.688], [0.22, 0.64])

# x4 = ([-1, -1], [0.338, 0.7], [0.36, 0.712], [0.42, 0.708])

# Valores não participantes do treinamento do perceptron
# x3 = ([-1, -1], [0.28, 0.68], [0.236, 0.66], [0.22, 0.6])

# x4 = ([-1, -1], [0.32, 0.692], [0.32, 0.696], [0.32, 0.712])

x3 = ([-1, -1], [0.24, 0.688], [0.28, 0.72], [0.32, 0.76])

x4 = ([-1, -1], [0.28, 0.64], [0.356, 0.7], [0.42, 0.74])

# w = [0.22, -0.33, 0.44]
w = [0.3, -0.4, 0.5]

interacaoPerceptron(w)
verificaPerceptron(w, x3, x4)
