# main.py
from fastapi import FastAPI
import pandas as pd
from clustering import cluster_medicamentos
from simulation import simular_reposicao

app = FastAPI(title="HUSM - Previsão de Estoque")

@app.get("/")
def home():
    return {"message": "API de previsão de estoque do HUSM ativa!"}

@app.get("/cluster")
def get_clusters():
    dados = pd.read_csv("estoque.csv")
    dados_clustered = cluster_medicamentos(dados.rename(columns={"consumo_semanal": "consumo_mensal"}))
    resultado = simular_reposicao(dados_clustered, estoque_minimo=20)
    return resultado.to_dict(orient="records")
