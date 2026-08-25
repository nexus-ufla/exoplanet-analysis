# Passo a passo — do zero até o `exoplanets.csv`

Guia para quem está pegando o projeto pela primeira vez. Do clone do repositório até ter o
arquivo de dados na máquina, pronto para começar a análise.

Faça na ordem. Se algo der errado no meio, veja [Quando algo dá errado](#quando-algo-dá-errado)
no fim da página — não fique travado sozinho, mande no grupo.

> **Onde tudo isso acontece:** no terminal. No VS Code, abra com `Ctrl + '` (ou
> `Terminal → New Terminal`). Cada bloco de código abaixo é **um comando** — copie, cole,
> aperte Enter, espere terminar, e só então vá para o próximo.

---

## 1. Clonar o repositório

Clonar = baixar uma cópia do projeto do GitHub para o seu computador.

Primeiro, vá para a pasta onde você quer guardar o projeto (Documentos, por exemplo):

```bash
cd ~/Documentos
```

Agora clone:

```bash
git clone https://github.com/Nexus-UFLA/exoplanet-analysis.git
```

Isso cria uma pasta `exoplanet-analysis`. Entre nela:

```bash
cd exoplanet-analysis
```

**A partir daqui, todos os comandos são rodados de dentro dessa pasta.** Se você fechar o
terminal e voltar depois, precisa dar o `cd` de novo.

Confira que deu certo:

```bash
ls
```

Você deve ver `README.md`, `main.py`, `src/`, `notebooks/`, `docs/`.

> **Já clonou antes?** Não clone de novo. Entre na pasta e atualize:
> ```bash
> git checkout main
> ```
> ```bash
> git pull
> ```

---

## 2. Criar a sua branch

Branch é uma linha de trabalho separada. Cada dupla trabalha na sua, e **ninguém commita
direto na `main`** — essa é a regra do grupo (ver [como-trabalhamos.md](como-trabalhamos.md)).

Antes de criar, garanta que você está partindo da `main` atualizada:

```bash
git checkout main
```

```bash
git pull
```

Agora crie a sua branch. Troque o nome pelo da **sua pergunta**:

```bash
git checkout -b modulo1-linha-do-tempo
```

O `-b` significa "crie e já mude para ela". Nomes das branches do Módulo 1:

| Dupla | Pergunta | Nome da branch |
|---|---|---|
| 1 | Descobertas por ano | `modulo1-linha-do-tempo` |
| 2 | Métodos por época | `modulo1-metodos-por-epoca` |
| 3 | Método × tipo de planeta | `modulo1-metodo-vs-planeta` |
| 4 | Observatórios e missões | `modulo1-observatorios` |

Confira em qual branch você está:

```bash
git branch
```

O asterisco `*` marca a branch atual. Tem que ser a sua, não a `main`.

> **A branch já existe** (seu colega criou e subiu)? Aí não use `-b`, só entre nela:
> ```bash
> git fetch
> ```
> ```bash
> git checkout modulo1-linha-do-tempo
> ```

---

## 3. Criar o ambiente virtual

O ambiente virtual (`venv`) é uma "caixinha" onde as bibliotecas do projeto ficam instaladas
sem bagunçar o resto do seu Python.

Crie (só na primeira vez):

```bash
python -m venv .venv
```

Ative — **isso precisa ser feito toda vez que você abrir o terminal**:

No Windows (PowerShell):

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Deu certo quando aparece `(.venv)` no começo da linha do terminal. Se não apareceu, o
ambiente não está ativo e o passo seguinte vai instalar as bibliotecas no lugar errado.

---

## 4. Instalar as bibliotecas

```bash
pip install -r requirements.txt
```

Demora alguns minutos na primeira vez. Instala pandas, numpy, matplotlib, seaborn e requests.

---

## 5. Baixar os dados

Este é o passo que gera o CSV:

```bash
python main.py
```

O que acontece por trás: o script monta uma consulta, envia para a **API TAP do NASA
Exoplanet Archive**, recebe a tabela em CSV e salva em `data/raw/exoplanets.csv`. Se a pasta
`data/raw/` não existir, ele cria.

Leva de 30 segundos a 2 minutos, dependendo da internet. **Não é normal ser instantâneo** —
se voltou na hora, provavelmente deu erro.

Quando termina, aparecem no terminal as primeiras 5 linhas da tabela, mais ou menos assim:

```
     pl_name    hostname  pl_orbper  pl_orbsmax  ...  disc_year
0  11 Com b     11 Com    326.03000      1.2900  ...       2007
1  11 UMi b     11 UMi    516.21997      1.5300  ...       2009
2  14 And b     14 And    186.76000      0.8300  ...       2008
...
```

Viu isso? **Deu certo.** O arquivo está em `data/raw/exoplanets.csv`.

### Conferindo o arquivo

```bash
python -c "import pandas as pd; df = pd.read_csv('data/raw/exoplanets.csv'); print(df.shape); print(df.columns.tolist())"
```

Você deve ver algo como `(6354, 24)` — cerca de **6.300 planetas** (o número cresce com o
tempo, novos planetas são confirmados toda semana) e **24 colunas**.

> **O CSV não vai para o Git.** A pasta `data/` está no `.gitignore` de propósito: dado
> baixado não se versiona, se rebaixa. Por isso cada pessoa roda esse passo na sua máquina.
> Se você e um colega rodarem em semanas diferentes, podem ter contagens ligeiramente
> diferentes — isso é esperado, e vale registrar a data em que vocês baixaram.

---

## 6. Abrir a análise

```bash
jupyter notebook
```

Ou simplesmente abra o arquivo `.ipynb` direto no VS Code.

Comece pelo `notebooks/01_eda.ipynb` para se ambientar. Depois vá para o notebook da sua
dupla em `notebooks/modulo1_vies/` (roteiro em
[notebooks/modulo1_vies/README.md](../notebooks/modulo1_vies/README.md)).

**Importante:** escolha o kernel do `.venv` no canto superior direito do VS Code. Se escolher
outro Python, as bibliotecas não vão ser encontradas.

---

## O que tem dentro do CSV

Uma linha por planeta, 24 colunas. As principais:

| Coluna | O que é | Unidade |
|---|---|---|
| `pl_name` | Nome do planeta | texto |
| `hostname` | Estrela hospedeira | texto |
| `pl_orbper` | Período orbital (o "ano" do planeta) | dias |
| `pl_orbsmax` | Distância até a estrela | UA (1 UA = Terra–Sol) |
| `pl_rade` | Raio do planeta | raios terrestres |
| `pl_bmasse` | Massa do planeta | massas terrestres |
| `pl_eqt` | Temperatura de equilíbrio | Kelvin |
| `st_teff` | Temperatura da estrela | Kelvin |
| `sy_dist` | Distância até nós | parsecs |
| `discoverymethod` | Como foi descoberto | texto |
| `disc_year` | Ano da descoberta | ano |
| `disc_facility` | Telescópio/missão | texto |

A lista completa, com comentário em cada coluna, está no topo de
[src/data_fetch.py](../src/data_fetch.py). O dicionário oficial da NASA está
[aqui](https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html).

### Duas decisões da consulta que vocês precisam entender

**1. `default_flag = 1`** — a tabela `ps` da NASA guarda **várias linhas para o mesmo
planeta**, uma para cada artigo científico que já mediu seus parâmetros. Sem esse filtro, o
mesmo planeta apareceria dezenas de vezes e toda contagem sairia errada. A NASA marca com
`default_flag = 1` a linha que ela considera o conjunto de parâmetros oficial daquele planeta.

**2. Não filtramos por raio nem por período.** Baixamos todos os planetas confirmados,
inclusive os que têm campos vazios. Planetas descobertos por velocidade radial quase nunca
têm raio medido — se a consulta já os descartasse, eles sumiriam do catálogo e a análise de
viés observacional do Módulo 1 daria a resposta errada. **Cada módulo aplica o filtro que
precisa, depois** — e explicando por quê.

---

## Quando algo dá errado

| Erro no terminal | O que significa | O que fazer |
|---|---|---|
| `'git' não é reconhecido...` | Git não instalado | Instale de [git-scm.com](https://git-scm.com/downloads) e **feche e reabra o terminal** |
| `'python' não é reconhecido...` | Python fora do PATH | Reinstale marcando "Add Python to PATH". No Linux/macOS tente `python3` |
| `No such file or directory: 'main.py'` | Você está na pasta errada | `cd exoplanet-analysis` |
| `ModuleNotFoundError: No module named 'requests'` | Ambiente não ativo ou libs não instaladas | Ative o `.venv` (passo 3) e rode o `pip install` (passo 4) |
| `Erro ao acessar a API: ... timeout` | Internet lenta ou site da NASA fora do ar | Espere alguns minutos e rode `python main.py` de novo |
| `Erro ao acessar a API: ... 400` | A consulta foi rejeitada | Alguém mexeu na lista de colunas? Confira o `git status` e avise no grupo |
| `execution of scripts is disabled` (Windows) | Política do PowerShell bloqueia o `activate` | Rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e responda `S` |
| CSV com 0 linhas ou só o cabeçalho | Download veio vazio | Apague `data/raw/exoplanets.csv` e rode `python main.py` de novo |

### Plano B: baixar pelo site

Se a API não colaborar no dia da reunião, dá para pegar os dados pelo navegador:

1. Acesse o [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/).
2. Vá em **Data → Planetary Systems** (tabela `ps`).
3. Use **Download Table → CSV format**, com **"Values for default parameter set only"**
   marcado — é o equivalente ao nosso `default_flag = 1`.
4. Salve como `data/raw/exoplanets.csv` (crie as pastas se não existirem).

O arquivo vem com **muito mais colunas** que as 24 do script e com linhas de comentário
começando com `#` no topo. Para ler, use `pd.read_csv(caminho, comment='#')` e selecione as
colunas que interessam. Prefira sempre o `python main.py` — o plano B é só para não travar a
reunião.

---

## Resumo (a cola)

Do zero, uma vez só:

```bash
git clone https://github.com/Nexus-UFLA/exoplanet-analysis.git
```

```bash
cd exoplanet-analysis
```

```bash
git checkout -b modulo1-linha-do-tempo
```

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

Nos dias seguintes, só isto: entrar na pasta, ativar o `.venv`, conferir a branch com
`git branch` e trabalhar. Baixar os dados de novo, só se quiser atualizar o catálogo.
