# Como trabalhamos

Grupo de **9 pessoas**. Todos os módulos funcionam do mesmo jeito.

---

## Os papéis

São só dois.

**Analistas** — as 8 pessoas das 4 duplas. São elas que respondem as perguntas do módulo.

**Gestor** — a pessoa que fica fora das duplas. É dela toda a responsabilidade de condução:

- organizar a reunião e conduzir a divisão das perguntas
- revisar os PRs e integrar tudo na `main`
- cuidar da documentação e do README
- registrar as decisões na ata (`meeting_notes.md`)
- apresentar o resultado do módulo

O gestor **não analisa** naquele módulo — a função dele é fazer o trabalho dos outros oito
chegar junto e organizado.

> O passo a passo do que fazer em cada etapa está no [Guia do Gestor](guia-do-gestor.md).

---

## Como cada módulo funciona

Sempre o mesmo ciclo, em três etapas:

### 1. Reunião de abertura (juntos)

- O gestor apresenta o módulo e suas perguntas
- Definir quem forma cada dupla e qual pergunta cada uma pega
- Preparar os dados **uma vez só**, em conjunto, e guardar em `src/`

### 2. Durante a semana (em duplas)

Cada dupla responde sua pergunta no próprio notebook, na própria branch. O gestor acompanha,
revisa os PRs e destrava quem emperrar.

### 3. Reunião de fechamento (juntos)

- Cada dupla apresenta sua figura em 5 minutos
- O grupo discute as diferenças de abordagem
- O gestor monta o `99_consolidado.ipynb` com a história completa

---

## As duplas

Com 9 pessoas: **4 duplas + 1 gestor**. Se o módulo tiver só 3 perguntas, uma das duplas vira
um trio.

Duas regras que fazem a dupla funcionar:

- **Junte um membro experiente com um novo.** É assim que o grupo se nivela — quem tem mais
  prática explica, quem tem menos pergunta.
- **Quem digita, de preferência, é quem sabe menos.** É quem mais aprende. Troquem o teclado
  ao longo do trabalho.

---

## Presença é variável

Com grupo grande, sempre vai faltar alguém. Desenhem as tarefas para que **nenhuma dependa de
uma pessoa específica**. É mais um motivo para a lógica compartilhada morar em `src/*.py`,
acessível a todos, em vez de dentro do notebook de quem não apareceu.

---

## Regras de Git

Um notebook `.ipynb` é um arquivo JSON com os resultados embutidos. **Se duas pessoas editam o
mesmo notebook, o conflito é quase certo e é bem chato de resolver.** Para evitar:

1. **Um notebook por dupla.** Nunca duas duplas no mesmo arquivo.
2. **Lógica compartilhada vai para `src/*.py`.** Arquivo `.py` tem merge limpo; notebook não.
   O notebook fica fino: chama as funções e conta a história.
3. **Limpar os resultados antes de commitar** (`Kernel → Restart & Clear Output`). Reduz muito
   o tamanho do diff e a chance de conflito.
4. **Uma branch por dupla**, com nome claro: `modulo1-linha-do-tempo`.
5. **Nada direto na `main`.** Sempre PR, sempre revisado pelo gestor.

### Fluxo básico

```bash
git checkout main
git pull
git checkout -b modulo1-linha-do-tempo
# ... trabalha, commita ...
git push -u origin modulo1-linha-do-tempo
# abre o PR no GitHub e pede revisão
```

---

## Estrutura de pastas

Uma pasta por módulo, um notebook por dupla:

```
notebooks/modulo1_vies/
├── README.md                   # o roteiro do módulo
├── 01_linha_do_tempo.ipynb     # dupla 1
├── 02_metodos_por_epoca.ipynb  # dupla 2
├── 03_metodo_vs_planeta.ipynb  # dupla 3
├── 04_observatorios.ipynb      # dupla 4
└── 99_consolidado.ipynb        # montado junto, na reunião
src/
└── vies.py                     # funções compartilhadas (merge limpo aqui)
```

---

## Definição de pronto (vale para todo módulo)

- [ ] Os notebooks rodam de ponta a ponta, sem erro, na máquina de outra pessoa
- [ ] Cada gráfico tem título, eixos nomeados e unidades
- [ ] Cada notebook termina com uma conclusão escrita em linguagem simples
- [ ] Pelo menos uma figura salva em `reports/figures/`
- [ ] Tudo integrado na `main` via PR revisado
- [ ] Decisões e dúvidas registradas em `meeting_notes.md`
