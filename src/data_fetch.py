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

# Colunas usadas pelos módulos de análise do projeto.
# Cada grupo abaixo alimenta uma frente diferente (ver docs/roadmap.md).
COLUNAS = [
    # identificação
    "pl_name",          # nome do planeta
    "hostname",         # nome da estrela hospedeira
    # órbita e clima do planeta
    "pl_orbper",        # período orbital (dias)
    "pl_orbsmax",       # distância orbital / semi-eixo maior (UA)
    "pl_orbeccen",      # excentricidade da órbita
    "pl_insol",         # fluxo de energia recebido (em unidades da Terra)
    "pl_eqt",           # temperatura de equilíbrio (K)
    # propriedades do planeta
    "pl_rade",          # raio (raios terrestres)
    "pl_bmasse",        # massa (massas terrestres)
    "pl_dens",          # densidade (g/cm3)
    "pl_radeerr1",      # incerteza do raio (para cima)
    "pl_radeerr2",      # incerteza do raio (para baixo)
    # propriedades da estrela
    "st_teff",          # temperatura efetiva (K)
    "st_rad",           # raio (raios solares)
    "st_mass",          # massa (massas solares)
    "st_lum",           # luminosidade (log10, em unidades solares)
    "st_met",           # metalicidade
    "st_age",           # idade (bilhões de anos)
    # sistema e descoberta
    "sy_snum",          # número de estrelas no sistema
    "sy_pnum",          # número de planetas no sistema
    "sy_dist",          # distância até nós (parsecs)
    "discoverymethod",  # método de descoberta
    "disc_year",        # ano da descoberta
    "disc_facility",    # observatório/missão que descobriu
]


def fetch_exoplanet_data(save_path="data/raw/exoplanets.csv"):
    """Baixa a tabela de exoplanetas e salva em `save_path`.

    Retorna um DataFrame do pandas com uma linha por planeta.

    Sobre `default_flag`:
    a tabela "ps" guarda VÁRIAS linhas para o mesmo planeta — uma para cada
    artigo científico que já mediu seus parâmetros. Se não filtrarmos, o mesmo
    planeta aparece dezenas de vezes. A coluna `default_flag = 1` marca a linha
    que a NASA escolheu como o conjunto de parâmetros "oficial" de cada planeta,
    então filtramos por ela para ter um registro por planeta.

    Por que NÃO filtramos por raio/período aqui:
    baixamos TODOS os planetas confirmados, mesmo os que não têm raio medido.
    Planetas descobertos por velocidade radial, por exemplo, quase nunca têm
    raio — se filtrássemos por raio na consulta, eles sumiriam e a análise de
    viés observacional (módulo 1) ficaria errada. Cada módulo aplica o filtro
    que precisa, depois.
    """
    # garante que a pasta de destino existe
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # query sem indentação (evita problemas de encoding na URL)
    query = "SELECT " + ", ".join(COLUNAS) + " FROM ps WHERE default_flag = 1"

    params = {
        "query": query,
        "format": "csv",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=180)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Erro ao acessar a API: {e}")

    # salva o arquivo bruto
    with open(save_path, "wb") as f:
        f.write(response.content)

    # carrega o DataFrame a partir do arquivo salvo
    df = pd.read_csv(save_path)

    return df
