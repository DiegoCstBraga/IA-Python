from Perce import interacaoPerceptron, verificaPerceptron

# Valores usados no treinamento do Perceptron
# x3 = ([0.2, 0.64], [0.24, 0.68], [0.28, 0.72], [0.32, 0.76])

# x4 = ([0.28, 0.64], [0.32, 0.68], [0.36, 0.72], [0.42, 0.76])

# Valores não participantes do treinamento do perceptron
# x3 = ([0.0, 0.0], [0.28, 0.68], [0.236, 0.66], [0.22, 0.6])

# x4 = ([0.0, 0.0], [0.32, 0.692], [0.32, 0.696], [0.32, 0.712])

# Segundo teste dos valores não participantes do treinamento do perceptron
x3 = ([0.0, 0.0], [0.24, 0.692], [0.3, 0.72], [0.18, 0.6],
      [0.28, 0.68], [0.252, 0.716], [0.22, 0.6])

x4 = ([0.0, 0.0], [0.36, 0.692], [0.52, 0.76], [0.36, 0.68],
      [0.36, 0.712], [0.32, 0.696], [0.32, 0.712])


w = [-0.22, 0.33, -0.44]

interacaoPerceptron(w)
verificaPerceptron(w, x3, x4)
