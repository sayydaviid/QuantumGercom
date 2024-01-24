from utils import prepara_amostra_problema

sample, _ = prepara_amostra_problema(seed=42)
print("Amostra:")
print(sample.to_string(index=False))