import numpy as np

def carrega_problema_qubo(seed=42, size=5):
    np.random.seed(seed)

    # Criando uma matriz simétrica aleatória para representar o QUBO
    qubo_matrix = np.random.randint(low=-5, high=5, size=(size, size))
    qubo_matrix = (qubo_matrix + qubo_matrix.T) / 2  # Tornando a matriz simétrica

    # Atribuindo pesos aleatórios para os termos lineares
    linear_terms = np.random.randint(low=-5, high=5, size=size)

    return qubo_matrix, linear_terms