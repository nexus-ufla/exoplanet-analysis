# Análise e Detecção de Exoplanetas

Projeto colaborativo de ciência de dados aplicada a dados astronômicos reais e públicos
do [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/).

O objetivo de longo prazo é construir, passo a passo, um **classificador de trânsitos de
exoplanetas** — um programa que identifica, no brilho de uma estrela ao longo do tempo, a
assinatura de um planeta passando na frente dela. É um projeto de processamento de sinal +
machine learning sobre dado científico de verdade.

> 📍 **Estamos começando pela base.** Antes de mexer em curvas de luz e modelos, vamos
> primeiro dominar os dados e as ferramentas com uma **análise exploratória (EDA)** de
> planetas confirmados. O caminho completo está em [docs/roadmap.md](docs/roadmap.md).

## Estado atual — Fase 0 (EDA de catálogo)

Nesta fase trabalhamos com uma tabela de planetas já confirmados para praticar Python,
pandas, gráficos e Git, e entender as grandezas físicas que importarão depois:

- Coleta dos dados via API do NASA Exoplanet Archive.
- Limpeza e tratamento (duplicatas, valores ausentes, valores extremos).
- Análise exploratória: distribuições, relações entre variáveis, classificação por tamanho.
- Primeira triagem exploratória de planetas potencialmente interessantes.

O que vem depois (curvas de luz, BLS, redes neurais) está descrito no roadmap — **sem
pressa**, uma fase por vez.

## Estrutura do projeto

```
exoplanet-analysis/
├── README.md
├── requirements.txt
├── main.py                 # baixa os dados e mostra uma prévia
├── data/
│   ├── raw/                # dados baixados (não versionados)
│   └── processed/          # dataset limpo, gerado pela análise
├── notebooks/
│   └── 01_eda.ipynb        # análise exploratória (comece por aqui)
├── src/
│   ├── data_fetch.py       # coleta dos dados da API
│   ├── preprocessing.py    # limpeza dos dados
│   └── visualization.py    # funções de gráfico reaproveitáveis
├── docs/
│   ├── roadmap.md          # os módulos de análise do projeto
│   ├── como-trabalhamos.md # divisão de tarefas, papéis e regras de Git
│   ├── referencias.md      # links e materiais de apoio
│   └── meeting_notes.md    # atas de reunião
└── reports/
    └── figures/            # figuras exportadas da análise
```

## Como executar

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd exoplanet-analysis
```

### 2. Criar e ativar um ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Baixar os dados

```bash
python main.py
```

Isso usa `fetch_exoplanet_data()` para consultar a API, salvar os dados em
`data/raw/exoplanets.csv` e mostrar uma prévia.

### 5. Aquecimento opcional de EDA

Antes de entrar nos dados de exoplanetas, existe um material introdutório com dados físicos
históricos, mas sem usar exoplanetas:

- roteiro da aula: `docs/aula_eda_intro.md`
- notebook: `notebooks/00_aquecimento_eda.ipynb`
- dados: `data/sample/hubble_1929_galaxias.csv`

Use esse aquecimento para apresentar EDA, pandas, unidades, dispersão, reta de tendência e
interpretação cuidadosa de dados reais.

### 6. Abrir a análise

Abra `notebooks/01_eda.ipynb` no Jupyter ou no VS Code e execute as células de cima para baixo.

## Fonte dos dados

Os dados vêm da API TAP do NASA Exoplanet Archive. A consulta usa `default_flag = 1` para
trazer **um registro por planeta** (a tabela guarda várias linhas por planeta, uma para cada
artigo publicado). Colunas coletadas:

| Coluna | Descrição | Unidade |
| --- | --- | --- |
| `pl_name` | Nome do planeta | texto |
| `pl_rade` | Raio do planeta | raios terrestres |
| `pl_bmasse` | Massa do planeta | massas terrestres |
| `pl_orbper` | Período orbital | dias |
| `st_teff` | Temperatura efetiva da estrela | Kelvin |

## Organização do grupo

Projeto desenvolvido de forma colaborativa, com ritmo calmo e revisão coletiva — pensado
também para nivelar membros que entraram recentemente.

**Cada módulo de análise é explorado pelo grupo inteiro, junto.** O que dividimos é o
trabalho dentro de cada módulo — os papéis, o modo de trabalho e as regras de Git estão em
[docs/como-trabalhamos.md](docs/como-trabalhamos.md).

- **Reuniões:** uma por semana (presencial ou online); comunicação contínua por Trello/WhatsApp.
- **Papéis rotativos:** todos são analistas; a cada módulo, quatro pessoas assumem um papel
  extra (coordenador, documentador, escriba, apresentador).
- **Revisão coletiva:** nada entra na `main` sem PR revisado por outra pessoa.
- **Atas:** registrar decisões em [docs/meeting_notes.md](docs/meeting_notes.md).

## Próximos passos

Veja o [roadmap](docs/roadmap.md). Em resumo: terminar a **Fase 0** (EDA base) com
tranquilidade e, na sequência, atacar o **Módulo 1 — Viés observacional** com o grupo todo
junto (roteiro em [notebooks/modulo1_vies/README.md](notebooks/modulo1_vies/README.md)).
