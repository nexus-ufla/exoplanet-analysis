# Roadmap do Projeto

Este documento é o **mapa do projeto**: mostra as frentes de trabalho, o que cada uma
investiga e o que se aprende fazendo.

**Cada módulo é explorado pelo grupo inteiro, junto.** Não existe "dono" de módulo — o que
dividimos é o trabalho *dentro* de cada um. Como fazemos essa divisão na prática está em
[como-trabalhamos.md](como-trabalhamos.md).

## A ideia geral

Estudamos exoplanetas — planetas fora do Sistema Solar — usando dados públicos e reais do
[NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/). Já são mais de 6 mil
planetas confirmados, com informações sobre tamanho, massa, órbita e sobre as estrelas que
eles orbitam.

O projeto não tem um único objetivo: tem **várias perguntas** que dá para responder com
esses dados. Cada módulo abaixo é uma dessas perguntas.

---

## Fase 0 — Base comum (todos passam por aqui)

**Onde estamos.** Antes de qualquer módulo, todo mundo faz a análise exploratória em
`notebooks/01_eda.ipynb` para se familiarizar com os dados, o Python e o Git.

**Pronto quando:** o grupo consegue carregar os dados, limpar, fazer gráficos e explicar o
que as quatro variáveis principais significam.

---

## Módulos temáticos

Depois da Fase 0, o grupo pega **um módulo por vez, todos juntos**. Cada módulo vira uma
pasta em `notebooks/`.

### Módulo 1 — Viés observacional (recomendado começar por aqui)

> **Pergunta:** por que os primeiros planetas descobertos eram quase todos gigantes e
> colados na estrela? Isso diz algo sobre o universo ou sobre os nossos telescópios?

Este é o módulo mais fácil — os dados de descoberta estão **100% preenchidos**, sem valores
faltando para atrapalhar. E ensina a lição mais importante do projeto: **o catálogo não é o
universo, é o que conseguimos detectar**. Sem entender isso, qualquer conclusão dos outros
módulos sai torta.

- **Colunas:** `discoverymethod`, `disc_year`, `disc_facility`, `pl_rade`, `pl_orbper`
- **Caminho:** linha do tempo de descobertas por ano → quais métodos dominam cada época →
  comparar o tipo de planeta que cada método encontra → discutir por que
- **Aprende:** agrupamento no pandas, gráficos de série temporal, e raciocínio científico
  sobre viés de seleção
- **Nível:** iniciante — ideal para quem entrou agora

### Módulo 2 — Habitabilidade

> **Pergunta:** quais planetas estão na distância certa da estrela para ter água líquida?

- **Colunas:** `st_teff`, `st_rad`, `st_mass`, `pl_orbper`, `pl_orbsmax`, `pl_rade`
- **Caminho:** calcular a luminosidade da estrela (Stefan-Boltzmann) → obter a distância
  orbital (3ª lei de Kepler) → calcular quanta energia o planeta recebe → comparar com os
  limites da zona habitável → montar um ranking de planetas parecidos com a Terra
- **Detalhe importante:** a coluna pronta de insolação (`pl_insol`) só existe para 15% dos
  planetas. Calculando nós mesmos a partir de colunas bem preenchidas, chegamos a ~85%.
  Isso é física de verdade e multiplica por 5 o tamanho da amostra.
- **Aprende:** traduzir fórmula física em código, propagar cálculos em colunas
- **Nível:** intermediário

> ⚠️ **Cuidado conceitual:** "zona habitável" quer dizer que a *distância* é favorável à
> água líquida. Não diz nada sobre atmosfera, campo magnético ou vida. É ponto de partida,
> nunca conclusão. Escrevam isso nos gráficos e no relatório.

### Módulo 3 — Composição planetária e o "vale do raio"

> **Pergunta:** os planetas se distribuem em tamanhos contínuos, ou existem tamanhos
> "proibidos"?

O melhor momento "uau" do projeto: existe uma escassez real de planetas com raio entre
~1,5 e ~2 raios terrestres — o **vale do raio**, descoberto em 2017. Dá para reencontrá-lo
nos dados com um histograma bem feito.

- **Colunas:** `pl_rade`, `pl_bmasse`, `pl_dens`, `pl_radeerr1/err2`
- **Caminho:** calcular densidade → separar rochosos de gasosos → histograma de raios numa
  amostra com medidas precisas → procurar o vale
- **Detalhe:** o vale só aparece se filtrarem planetas com raio bem medido. Com todo o
  catálogo junto, o ruído das medidas imprecisas apaga o sinal — o que já é uma boa lição.
- **Aprende:** histogramas e escolha de faixas, filtrar por qualidade de medida
- **Nível:** intermediário

### Módulo 4 — Estrelas hospedeiras

> **Pergunta:** o tipo de estrela influencia os planetas que ela tem?

Reproduz um resultado publicado de verdade: estrelas **ricas em metais** têm mais chance de
abrigar planetas gigantes.

- **Colunas:** `st_teff`, `st_mass`, `st_met`, `st_age`, `sy_pnum`, `pl_rade`
- **Caminho:** classificar estrelas por temperatura (tipo espectral) → comparar metalicidade
  entre estrelas com e sem planetas gigantes → verificar se a diferença é real
- **Aprende:** comparação entre grupos, noções de significância
- **Nível:** intermediário

### Módulo 5 — Curvas de luz e trânsitos (avançado)

> **Pergunta:** dá para detectar um planeta a partir do brilho bruto da estrela?

A frente mais difícil, e a mais próxima de pesquisa real. Fica para quando o grupo estiver
maduro nos módulos anteriores.

- **Ferramenta:** `lightkurve` (baixa curvas de luz das missões Kepler e TESS)
- **Caminho:** baixar a curva de uma estrela conhecida (Kepler-10) → limpar → remover a
  tendência lenta do brilho → achar o período com Box Least Squares → dobrar a curva em fase
  até o trânsito aparecer
- **Depois disso:** montar um conjunto de dados com muitas estrelas e treinar um
  classificador que separa trânsitos reais de falsos positivos
- **Aprende:** séries temporais, filtragem de sinal, e (mais adiante) machine learning
- **Nível:** avançado

---

## Ordem dos módulos

**Módulo 1 primeiro**, com o grupo todo junto. Ele é o mais fácil e dá o contexto que os
outros usam — quem analisa habitabilidade sem entender viés observacional acaba concluindo
que planetas habitáveis são raros, quando na verdade eles são só *difíceis de detectar*.

Depois: 2, 3 e 4 conforme o interesse do grupo. O 5 fica para quando houver maturidade.

Cada módulo termina com:
- notebooks que rodam de ponta a ponta e se explicam sozinhos,
- pelo menos uma figura salva em `reports/figures/`,
- um parágrafo de conclusão em linguagem simples,
- uma apresentação curta do que foi descoberto, na reunião.

O detalhe de **como dividir o trabalho** dentro do módulo está em
[como-trabalhamos.md](como-trabalhamos.md).

## Glossário rápido

- **Trânsito:** queda no brilho quando o planeta passa na frente da estrela.
- **Curva de luz:** brilho da estrela medido ao longo do tempo.
- **Insolação:** quanta energia o planeta recebe, comparada à Terra (1 = igual à Terra).
- **Zona habitável:** faixa de distâncias onde água líquida poderia existir na superfície.
- **Metalicidade:** quanto de elementos além de hidrogênio e hélio a estrela tem.
- **Viés observacional:** quando o que observamos reflete o limite do instrumento, não a
  realidade.
