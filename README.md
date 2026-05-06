# Projeto de Análise de Dados de Exoplanetas

Este projeto tem como objetivo explorar e analisar dados de exoplanetas confirmados usando dados públicos da NASA, disponíveis no NASA Exoplanet Archive:

https://exoplanetarchive.ipac.caltech.edu/

O foco principal é a análise de propriedades físicas de exoplanetas, exploração estatística dos dados, interpretação científica básica e desenvolvimento colaborativo em Python.

## Objetivos

- Analisar propriedades de exoplanetas confirmados.
- Estudar a distribuição de tamanhos dos planetas.
- Investigar possíveis candidatos a planetas habitáveis.
- Detectar padrões orbitais básicos.
- Construir visualizações e gráficos para interpretação dos dados.
- Praticar programação científica, análise de dados, Git/GitHub e trabalho colaborativo.

## Escopo

### Inclui

- Coleta de dados via API do NASA Exoplanet Archive.
- Tratamento e limpeza dos dados.
- Análise estatística exploratória.
- Criação de gráficos e visualizações.
- Interpretação básica de propriedades físicas e orbitais.

### Não inclui

- Treinamento de modelos de inteligência artificial.
- Simulações astrofísicas completas.
- Modelagem física avançada.

## Tecnologias

| Área | Ferramenta |
| --- | --- |
| Linguagem | Python |
| Dados | Pandas, NumPy |
| Visualização | Matplotlib |
| API | Requests |
| Versionamento | Git |
| Repositório | GitHub |

## Estrutura do Projeto

```bash
exoplanet-analysis/
|
|-- data/
|   |-- raw/
|   |   `-- exoplanets.csv
|   `-- processed/
|
|-- notebooks/
|
|-- src/
|   |-- data_fetch.py
|   |-- preprocessing.py
|   |-- analysis.py
|   |-- visualization.py
|   `-- utils.py
|
|-- results/
|
|-- docs/
|   |-- planning.md
|   |-- references.md
|   `-- meeting_notes.md
|
|-- requirements.txt
|-- README.md
`-- main.py
```

> Observação: algumas pastas e arquivos da estrutura planejada ainda podem ser criados conforme o avanço do projeto.

## Como Executar

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

### 4. Executar o projeto

```bash
python main.py
```

O script principal utiliza a função `fetch_exoplanet_data()` para consultar a API, salvar os dados em `data/raw/exoplanets.csv` e carregar o resultado como um DataFrame do Pandas.

## Fonte dos Dados

Os dados são coletados do NASA Exoplanet Archive por meio da API TAP:

```text
https://exoplanetarchive.ipac.caltech.edu/TAP/sync
```

Atualmente, a consulta coleta colunas como:

| Coluna | Descrição |
| --- | --- |
| `pl_name` | Nome do planeta |
| `pl_rade` | Raio do planeta em raios terrestres |
| `pl_bmasse` | Massa do planeta em massas terrestres |
| `pl_orbper` | Período orbital |
| `st_teff` | Temperatura efetiva da estrela |

## Organização do Grupo

O projeto será desenvolvido de forma colaborativa, sem divisão rígida de tarefas. Todos os membros participarão de:

- Programação.
- Análise dos dados.
- Interpretação física.
- Revisão de código.
- Documentação.

### Modelo de Trabalho

As etapas principais serão desenvolvidas em conjunto durante reuniões técnicas semanais. A cada etapa haverá um responsável temporário pela organização, com função de:

- Organizar commits.
- Integrar alterações.
- Revisar a estrutura dos arquivos.
- Documentar decisões importantes.

Essa responsabilidade será rotativa entre os membros.

### Revisão Coletiva

Toda funcionalidade implementada deverá:

- Ser explicada ao grupo.
- Passar por revisão coletiva.
- Ser integrada em conjunto.

## Organização Semanal

O grupo realizará uma reunião presencial ou online por semana e manterá comunicação contínua por Trello e WhatsApp.

### Trello

Será utilizado para:

- Organização das tarefas.
- Acompanhamento do progresso.
- Divisão das atividades da semana.
- Registro de pendências.

### WhatsApp

Será utilizado para:

- Comunicação rápida.
- Dúvidas.
- Alinhamentos curtos.
- Compartilhamento de atualizações.

## Cronograma Geral

| Semana | Foco Principal | Entregas |
| --- | --- | --- |
| 1 | Organização e estudo | Repositório, GitHub e estrutura inicial |
| 2 | API e coleta de dados | `data_fetch.py` funcionando |
| 3 | Limpeza e tratamento | Dataset tratado |
| 4 | Análise exploratória | Histogramas e estatísticas |
| 5 | Interpretação e visualização | Gráficos finais |
| 6 | Finalização | Relatório e apresentação |

## Planejamento Detalhado

### Semana 1 - Organização e nivelamento

Objetivos:

- Nivelar o conhecimento do grupo.
- Preparar o ambiente de desenvolvimento.
- Organizar a estrutura do projeto.

Entregas:

- Repositório criado.
- Branches definidas.
- Estrutura inicial pronta.
- Documento de planejamento finalizado.

### Semana 2 - API e coleta de dados

Objetivos:

- Entender a API.
- Coletar o dataset.
- Salvar os dados localmente.

Entregas:

- Conexão funcional com a API.
- Dataset salvo em `data/raw`.
- Script de coleta funcionando.

### Semana 3 - Limpeza e preparação

Objetivos:

- Preparar os dados para análise.
- Remover inconsistências.
- Tratar valores ausentes.

Entregas:

- Dataset limpo.
- Pipeline de limpeza funcional.
- Dados prontos para análise.

### Semana 4 - Análise exploratória

Objetivos:

- Entender padrões nos dados.
- Gerar primeiras interpretações.
- Criar histogramas, estatísticas descritivas e scatter plots.

Entregas:

- Gráficos iniciais.
- Estatísticas básicas.
- Primeiras interpretações.

### Semana 5 - Interpretação física e visualização

Objetivos:

- Relacionar resultados com conceitos físicos.
- Analisar habitabilidade de forma introdutória.
- Refinar gráficos e visualizações.

Entregas:

- Gráficos finais.
- Interpretação física consolidada.
- Visualizações prontas.

### Semana 6 - Finalização

Objetivos:

- Consolidar o projeto.
- Revisar código e documentação.
- Preparar relatório e apresentação.

Entregas:

- README final.
- Relatório.
- Apresentação.
- Repositório finalizado.

## Status Atual

- Estrutura inicial do projeto criada.
- Script `src/data_fetch.py` implementado para coleta de dados.
- Arquivo `data/raw/exoplanets.csv` disponível.
- Próximas etapas: limpeza dos dados, análise exploratória e visualizações.
