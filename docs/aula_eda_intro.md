# Aula introdutória: EDA com dados físicos

Este roteiro é um aquecimento antes do notebook principal de exoplanetas. O tema é a relação
distância-velocidade de galáxias no artigo clássico de Edwin Hubble, publicado em 1929.

Material de apoio:

- Dados: `data/sample/hubble_1929_galaxias.csv`
- Notebook: `notebooks/00_aquecimento_eda.ipynb`
- Fonte: NASA/APOD, reprodução do artigo "A Relation Between Distance and Radial Velocity
  Among Extra-Galactic Nebulae", de Edwin Hubble:
  <https://apod.nasa.gov/diamond_jubilee/1996/hub_1929.html>

## Por que esse exemplo funciona bem

Ele é físico, real e pequeno. Cada linha é uma galáxia ou sistema próximo, com:

- distância estimada em Mpc;
- velocidade radial em km/s;
- magnitude aparente visual (`mt`).

O dataset também tem características úteis para ensinar EDA:

- uma tendência clara, mas com muita dispersão;
- velocidades negativas em objetos próximos;
- uma amostra pequena;
- medições históricas, não definitivas;
- uma pergunta física simples: galáxias mais distantes tendem a se afastar mais rápido?

## Objetivo da aula

Ao final, o grupo deve conseguir:

- carregar uma tabela com `pandas`;
- entender linhas, colunas, tipos e unidades;
- fazer estatísticas descritivas simples;
- levantar perguntas antes de sair plotando gráficos;
- construir gráficos básicos e interpretá-los com cuidado;
- ajustar uma reta simples só como ferramenta exploratória;
- separar observação, modelo e conclusão.

## Mensagem principal

EDA não é "fazer vários gráficos". EDA é conversar com os dados:

1. O que cada linha representa?
2. O que cada coluna mede?
3. Quais unidades aparecem?
4. Existem valores inesperados?
5. Que padrões aparecem?
6. Que explicações são possíveis?
7. O que ainda não dá para afirmar?

## Roteiro sugerido para 60 minutos

### 1. Contexto físico - 5 min

Apresente a pergunta:

> Existe relação entre a distância de uma galáxia e a velocidade com que ela se afasta?

Explique só o necessário:

- velocidade radial positiva: objeto se afastando;
- velocidade radial negativa: objeto se aproximando;
- Mpc: megaparsec, unidade de distância astronômica;
- os dados são históricos e têm incertezas grandes.

### 2. Primeira inspeção - 10 min

Mostre:

- `df.head()`
- `df.shape`
- `df.info()`
- `df.describe()`

Ponto didático: antes de analisar, precisamos saber se a tabela faz sentido e quais unidades
estão envolvidas.

### 3. Perguntas exploratórias - 5 min

Antes dos gráficos, peça hipóteses:

- As velocidades são todas positivas?
- Galáxias mais distantes parecem ter velocidades maiores?
- Há objetos que fogem do padrão?
- Uma reta seria um bom primeiro modelo?

### 4. Distribuições - 10 min

Gráficos recomendados:

- histograma de `distancia_mpc`;
- histograma de `velocidade_km_s`;
- boxplot de velocidades.

Perguntas para a turma:

- A amostra tem mais objetos próximos ou distantes?
- Existem velocidades negativas?
- Existem valores muito altos em relação ao resto?

### 5. Relação distância-velocidade - 15 min

Gráfico principal:

- dispersão de `distancia_mpc` vs `velocidade_km_s`;
- reta de tendência.

Ponto didático: a reta ajuda a resumir o padrão, mas não apaga a dispersão. Em física real,
medidas têm ruído, incertezas, erros sistemáticos e efeitos locais.

### 6. Estimativa simples - 10 min

Mostre uma regressão linear simples:

> velocidade = inclinação * distância + intercepto

A inclinação fica em km/s/Mpc, a mesma unidade da constante de Hubble.

Ressalva importante:

> A estimativa histórica de Hubble era muito maior que o valor moderno porque as distâncias
> usadas na época estavam subestimadas. Para esta aula, o objetivo não é obter o valor atual,
> mas aprender o processo de exploração.

### 7. Fechamento - 5 min

Peça uma conclusão curta:

> O que os dados sugerem?
> O que eles não provam sozinhos?
> Que medições melhores ajudariam?

Exemplo de conclusão esperada:

> Nesta amostra histórica, galáxias mais distantes tendem a ter velocidades radiais maiores.
> A relação parece aproximadamente linear, mas há grande dispersão e objetos próximos com
> velocidade negativa. Isso sugere uma relação física importante, mas a amostra pequena e as
> incertezas das distâncias limitam a conclusão.

## Transição para exoplanetas

Depois da aula, conecte com o projeto:

- `distancia_mpc` e `velocidade_km_s` viram `pl_rade`, `pl_bmasse`, `pl_orbper` e `st_teff`;
- unidades continuam importantes;
- valores extremos continuam importantes;
- dispersão não significa ausência de padrão;
- uma relação visual não basta sem entender como o dado foi medido;
- a pergunta "o dado representa o universo ou o limite da observação?" continua central.
