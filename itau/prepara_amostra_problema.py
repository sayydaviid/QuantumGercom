
import numpy as np

def prepara_amostra_problema(seed=42, size=100):
    np.random.seed(seed)
    
    # Criando uma amostra aleatória
    sample = np.random.randn(size, 2)
    
    # Calculando a matriz de covariância da amostra
    cov_sample = np.cov(sample, rowvar=False)
    
    return sample, cov_sample
