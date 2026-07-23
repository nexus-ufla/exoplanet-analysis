"""Limpeza e preparação dos dados de exoplanetas.

Funções simples e reaproveitáveis para deixar o dataset pronto para a análise.
A ideia é manter o notebook enxuto: o notebook conta a história e chama estas
funções para fazer o trabalho pesado.
"""

import os
import pandas as pd

# colunas numéricas que usamos na análise
COLUNAS_NUMERICAS = ["pl_rade", "pl_bmasse", "pl_orbper", "st_teff"]


def remover_duplicatas(df, coluna_id="pl_name"):
    """Mantém apenas um registro por planeta.

    Mesmo baixando com `default_flag = 1`, pode sobrar algum nome repetido.
    Aqui garantimos, de forma simples, uma linha por planeta.
    """
    return df.drop_duplicates(subset=coluna_id, keep="first").reset_index(drop=True)


def remover_valores_invalidos(df, colunas=COLUNAS_NUMERICAS):
    """Remove linhas sem raio ou período (as duas variáveis essenciais).

    Massa (`pl_bmasse`) e temperatura (`st_teff`) têm muitos valores ausentes,
    então NÃO removemos linhas por causa delas — apenas por raio e período,
    que são o mínimo necessário para a análise.
    """
    essenciais = ["pl_rade", "pl_orbper"]
    df = df.dropna(subset=essenciais)
    # remove valores não-físicos (raio ou período <= 0)
    for coluna in essenciais:
        df = df[df[coluna] > 0]
    return df.reset_index(drop=True)


def limpar_dados(df):
    """Pipeline de limpeza completo: duplicatas + valores inválidos.

    Recebe o DataFrame bruto e devolve um DataFrame pronto para análise.
    """
    df = remover_duplicatas(df)
    df = remover_valores_invalidos(df)
    return df


def salvar_processado(df, caminho="data/processed/exoplanets_limpo.csv"):
    """Salva o dataset limpo em `data/processed/` (cria a pasta se preciso)."""
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    df.to_csv(caminho, index=False)
    return caminho
