import numpy as np

def gera_relatorio(seed=42, variaveis_resposta=None):
    np.random.seed(seed)

    if variaveis_resposta is None:
        raise ValueError("O array de variáveis de resposta não pode ser None.")

    # Número total de variáveis de resposta
    num_variaveis = len(variaveis_resposta)

    # Simula a geração de dados para o relatório
    dados_relatorio = np.random.rand(num_variaveis) * 10

    # Imprime o relatório
    print("Relatório Gerado:")
    for i, valor in enumerate(dados_relatorio):
        print(f"Variável {i+1}: {variaveis_resposta[i]} - Dado Relatório: {valor}")
