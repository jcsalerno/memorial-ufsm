# clustering.py
import pandas as pd
from sklearn.cluster import KMeans

def cluster_medicamentos(dados):
    """
    Aplica KMeans para identificar padrões de consumo e urgência de medicamentos.
    Espera um DataFrame pandas com colunas: ['medicamento', 'consumo_mensal', 'urgencia'].
    """
    X = dados[['consumo_mensal', 'urgencia']]

    modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
    dados['cluster'] = modelo.fit_predict(X)

    return dados
