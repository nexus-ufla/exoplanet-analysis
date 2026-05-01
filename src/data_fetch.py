import requests
import pandas as pd
import os

BASE_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

def fetch_exoplanet_data(save_path="data/raw/exoplanets.csv"):
    
    # garantir que a pasta existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # query sem indentação (evita problemas de encoding)
    query = (
        "SELECT pl_name, pl_rade, pl_bmasse, pl_orbper, st_teff "
        "FROM ps "
        "WHERE pl_rade IS NOT NULL "
        "AND pl_orbper IS NOT NULL"
    )

    params = {
        "query": query,
        "format": "csv"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao acessar a API: {e}")

    # salvar arquivo bruto
    with open(save_path, "wb") as f:
        f.write(response.content)

    # carregar DataFrame direto do conteúdo (mais seguro)
    df = pd.read_csv(save_path)

    return df