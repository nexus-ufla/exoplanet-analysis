"""Coleta de dados do NASA Exoplanet Archive.

Este módulo baixa a tabela de planetas confirmados (Planetary Systems, "ps")
usando a API TAP do NASA Exoplanet Archive e salva o resultado em CSV.

Documentação das colunas:
https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
"""

import os
import requests
import pandas as pd

BASE_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"


def fetch_exoplanet_data(save_path="data/raw/exoplanets.csv"):
    """Baixa a tabela de exoplanetas e salva em `save_path`.

    Retorna um DataFrame do pandas com uma linha por planeta.

    Observação importante sobre `default_flag`:
    a tabela "ps" guarda VÁRIAS linhas para o mesmo planeta — uma para cada
    artigo científico que já mediu seus parâmetros. Se não filtrarmos, o mesmo
    planeta aparece dezenas de vezes. A coluna `default_flag = 1` marca a linha
    que a NASA escolheu como o conjunto de parâmetros "oficial" de cada planeta,
    então filtramos por ela para ter um registro por planeta.
    """
    # garante que a pasta de destino existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # query sem indentação (evita problemas de encoding na URL)
    query = (
        "SELECT pl_name, pl_rade, pl_bmasse, pl_orbper, st_teff "
        "FROM ps "
        "WHERE default_flag = 1 "
        "AND pl_rade IS NOT NULL "
        "AND pl_orbper IS NOT NULL"
    )

    params = {
        "query": query,
        "format": "csv",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=60)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao acessar a API: {e}")

    # salva o arquivo bruto
    with open(save_path, "wb") as f:
        f.write(response.content)

    # carrega o DataFrame a partir do arquivo salvo
    df = pd.read_csv(save_path)

    return df
