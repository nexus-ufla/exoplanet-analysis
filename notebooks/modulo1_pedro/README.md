# Módulo 1 — Viés observacional

**Modo de trabalho:** 4 duplas, uma pergunta cada. Ver
[como-trabalhamos.md](../../docs/como-trabalhamos.md).

## A pergunta central

> Os primeiros exoplanetas descobertos eram quase todos gigantes e muito próximos da estrela.
> Isso acontece porque o universo é assim — ou porque eram os únicos que conseguíamos ver?

Essa distinção é o coração do módulo. A resposta muda como interpretamos **todos** os outros
módulos do projeto.

## Por que começamos por aqui

- **Os dados estão 100% preenchidos** (`discoverymethod`, `disc_year`, `disc_facility`,
  `sy_pnum`). Nenhum valor faltando para atrapalhar — perfeito para quem está começando.
- Dá o contexto que os outros módulos precisam. Sem ele, é fácil concluir que planetas
  parecidos com a Terra são *raros*, quando na verdade são só **difíceis de detectar**.

## As perguntas (uma por dupla)

| Dupla | Pergunta | Notebook |
|---|---|---|
| 1 | **Quantos planetas foram descobertos por ano?** Existe algum ano que explode no gráfico? O que aconteceu ali? | `01_linha_do_tempo.ipynb` |
| 2 | **Quais métodos de descoberta existem e qual domina cada época?** Os principais são trânsito e velocidade radial. A proporção mudou com o tempo? | `02_metodos_por_epoca.ipynb` |
| 3 | **Cada método encontra o mesmo tipo de planeta?** Comparem `pl_rade` e `pl_orbper` entre os métodos. Aqui mora a resposta da pergunta central. | `03_metodo_vs_planeta.ipynb` |
| 4 | **Quais observatórios/missões mais descobriram?** `disc_facility` — poucas missões respondem pela maior parte do catálogo. | `04_observatorios.ipynb` |

A **conclusão** — o que o catálogo diz sobre o universo e o que ele diz sobre nós — é montada
pelo grupo todo na reunião de fechamento, no `99_consolidado.ipynb`.

## Dicas (sem entregar o código)

- Os dados estão em `data/raw/exoplanets.csv`. Rodem `python main.py` se ainda não baixaram.
- Para as perguntas 1, 2 e 4 vocês vão precisar **contar ocorrências agrupando** por uma
  coluna. Procurem por `value_counts()` e `groupby()` no pandas.
- Funções que mais de uma dupla usar (carregar os dados, padronizar cores por método) vão
  para `src/vies.py`, não para dentro do notebook.
- Na pergunta 3, atenção: **nem todo planeta tem raio medido**. Planetas descobertos por
  velocidade radial quase nunca têm. Reparem no que isso significa antes de filtrar — e
  discutam se filtrar não estaria criando um viés *dentro* da análise de viés.
- Escalas logarítmicas ajudam muito quando os valores variam por muitas ordens de grandeza
  (já viram isso no `01_eda.ipynb`).

## Armadilhas conhecidas

- **Confundir "não existe" com "não foi medido".** Valor ausente não é valor zero.
- **Comparar contagens brutas entre épocas** sem lembrar que o esforço de observação mudou
  muito ao longo dos anos.
- **Concluir que um método é "melhor".** Eles são sensíveis a coisas diferentes — é aí que
  está o aprendizado.

## Na reunião de fechamento

Cada dupla apresenta sua figura em 5 minutos. Perguntas para guiar a discussão:

- As quatro respostas contam a **mesma história**?
- Alguma dupla filtrou dados que outra manteve? Qual decisão defende melhor a conclusão?
- Afinal: o catálogo diz mais sobre o universo ou sobre os nossos telescópios?

## Pronto quando

- [ ] As 4 perguntas respondidas com pelo menos um gráfico cada
- [ ] Cada gráfico com título, eixos nomeados e unidades
- [ ] Conclusão final escrita em conjunto no `99_consolidado.ipynb`
- [ ] Pelo menos uma figura salva em `reports/figures/`
- [ ] Notebooks integrados na `main` via PR
