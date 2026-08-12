"""Funções de visualização reaproveitáveis para a análise de exoplanetas.

Helpers simples em cima do matplotlib/seaborn. O objetivo é evitar repetir
código de gráfico no notebook e manter um estilo visual consistente.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def configurar_estilo():
    """Aplica um estilo visual limpo e padronizado."""
    sns.set_theme(style="whitegrid", context="notebook")


def plot_distribuicoes(df, colunas, bins=40, log=False):
    """Plota histogramas das colunas indicadas.

    Se `log=True`, usa log10 dos valores positivos (útil para dados
    astronômicos, que variam por muitas ordens de grandeza).
    """
    n = len(colunas)
    fig, axes = plt.subplots(1, n, figsize=(5 * n, 4))
    if n == 1:
        axes = [axes]

    for ax, coluna in zip(axes, colunas):
        dados = df[coluna].dropna()
        if log:
            dados = np.log10(dados[dados > 0])
            titulo = f"log10({coluna})"
        else:
            titulo = coluna
        sns.histplot(dados, bins=bins, kde=True, ax=ax)
        ax.set_title(f"Distribuição de {titulo}")
        ax.set_xlabel(titulo)
        ax.set_ylabel("Quantidade")

    plt.tight_layout()
    return fig


def salvar_figura(fig, caminho):
    """Salva uma figura em `reports/figures/` com boa resolução."""
    fig.savefig(caminho, dpi=150, bbox_inches="tight")
