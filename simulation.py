def simular_reposicao(df, estoque_minimo=20):
    """
    Simula reposição de estoque considerando estoque atual e urgência.
    - Estoque mínimo é ajustado: quanto maior a urgência, maior o estoque mínimo necessário.
    """
    df['estoque_minimo_ajustado'] = estoque_minimo + df['urgencia'] * 10
    df['repor'] = df['estoque_atual'] < df['estoque_minimo_ajustado']
    return df[['medicamento', 'estoque_atual', 'urgencia', 'cluster', 'estoque_minimo_ajustado', 'repor']]