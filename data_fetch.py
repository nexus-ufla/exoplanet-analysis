import requests
import pandas as pd
import os

BASE_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync"

def habitalidade_data(save_path="scr1data/planetas_habitaveis.csv"):

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    query = (
        "SELECT pl_name, pl_rade, pl_bmasse, pl_eqt, "
        "sy_dist, st_teff "
        "FROM ps "
        "WHERE pl_eqt IS NOT NULL "
        "AND pl_rade IS NOT NULL "
        "AND pl_bmasse IS NOT NULL "
        "AND sy_dist IS NOT NULL "
        "AND st_teff IS NOT NULL"
    )

    params = {
        "query": query,
        "format": "csv"
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        f.write(response.content)

    df = pd.read_csv(save_path)

    print(f"Número de linhas: {df.shape[0]}")
    print(f"Número de colunas: {df.shape[1]}")
    print("\nColunas:")
    print(df.columns.tolist())

    return df


df = habitalidade_data()

print("Primeiras linhas:")
print(df.head())