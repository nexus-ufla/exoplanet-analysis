# Referências e Recursos

## Dados

- **NASA Exoplanet Archive** — catálogo de planetas confirmados e tabela de KOIs (rótulos).
  https://exoplanetarchive.ipac.caltech.edu/
- **API TAP** (usada pelo `data_fetch.py` para baixar a tabela):
  https://exoplanetarchive.ipac.caltech.edu/TAP/sync
- **Dicionário de colunas da tabela PS:**
  https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html
- **MAST (Mikulski Archive for Space Telescopes)** — arquivo de onde as curvas de luz
  Kepler/TESS são baixadas (fases futuras).

## Ferramentas

- **lightkurve** — pacote Python oficial para curvas de luz Kepler/K2/TESS.
  https://docs.lightkurve.org/
- **Box Least Squares (BLS)** — busca de período de trânsito (`astropy.timeseries.BoxLeastSquares`).

## Leitura de fundo (fases futuras)

- **Shallue & Vanderburg (2018)**, *Identifying Exoplanets with Deep Learning*
  (The Astronomical Journal) — o artigo do AstroNet, base da arquitetura de rede neural
  que queremos reproduzir mais para frente.

## Conceitos rápidos

- **Método de trânsito:** medir a queda periódica no brilho da estrela quando o planeta passa.
- **Profundidade do trânsito ≈ (raio do planeta / raio da estrela)²** — planeta maior tampa
  mais luz.
- **Falsos positivos:** binárias eclipsantes, variabilidade estelar e artefatos do instrumento.
