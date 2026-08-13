# Guia do Gestor

O gestor é a pessoa que fica fora das duplas em um módulo. Ele não analisa dados — a função
dele é fazer o trabalho das 4 duplas chegar junto, organizado e integrado.

Este guia segue o ciclo do módulo, na ordem.

---

## 1. Antes da reunião de abertura

- [ ] Ler o `README.md` do módulo em `notebooks/<modulo>/` para saber quais são as perguntas
- [ ] Conferir se todos conseguem rodar `python main.py` e abrir o `01_eda.ipynb`
- [ ] Criar a pasta do módulo, se ainda não existir

---

## 2. Na reunião de abertura

- [ ] Apresentar o módulo: qual é a pergunta central e por que ela importa
- [ ] Formar as duplas — **sempre um membro mais experiente com um mais novo**
- [ ] Distribuir uma pergunta por dupla e anotar quem ficou com o quê
- [ ] Conduzir o preparo dos dados **em conjunto**, e guardar as funções em `src/`
- [ ] Combinar o prazo (normalmente até a próxima reunião)

**Anote na ata** (`docs/meeting_notes.md`): data, presentes, quem ficou com qual pergunta,
decisões tomadas e dúvidas que ficaram em aberto.

---

## 3. Durante a semana

Seu trabalho é **destravar e revisar**, não cobrar.

- [ ] Ficar disponível no grupo para dúvidas
- [ ] Conferir se as duplas criaram suas branches
- [ ] Revisar os PRs conforme forem chegando (não deixe acumular para o último dia)

### Como revisar um PR

Primeiro, rode o notebook da dupla na sua máquina:

```bash
git fetch origin
git checkout nome-da-branch-da-dupla
```

Abra o notebook, use `Kernel → Restart & Run All` e confira:

- [ ] Roda de ponta a ponta **sem erro**
- [ ] Os gráficos têm **título, eixos nomeados e unidades**
- [ ] Tem uma **conclusão escrita** em linguagem simples no fim
- [ ] A lógica que outras duplas também usam está em `src/`, não copiada no notebook
- [ ] Os resultados foram limpos antes do commit (`Restart & Clear Output`)

Se algo estiver faltando, comente no PR pedindo o ajuste. **Comentário de revisão explica o
porquê**, não só o quê: em vez de "falta título", escreva "coloca um título no gráfico, senão
quem abrir o notebook daqui a um mês não sabe o que está vendo".

### Como integrar

Quando estiver tudo certo, use o botão **"Merge pull request"** no GitHub. É o caminho mais
simples e deixa o histórico registrado.

---

## 4. Na reunião de fechamento

- [ ] Dar 5 minutos para cada dupla apresentar sua figura
- [ ] Puxar a discussão: as respostas contam a mesma história? Onde divergem, e por quê?
- [ ] Montar o `99_consolidado.ipynb` com o grupo — a história completa do módulo
- [ ] Escolher **pelo menos uma figura** para salvar em `reports/figures/`
- [ ] Registrar a conclusão do módulo na ata

---

## 5. Fechamento

- [ ] Todos os PRs integrados na `main`
- [ ] `99_consolidado.ipynb` na `main`
- [ ] Figuras salvas em `reports/figures/`
- [ ] Ata do módulo escrita
- [ ] README do projeto atualizado, se algo mudou
- [ ] Passar o bastão: combinar quem será o gestor do próximo módulo

---

## Comandos que você vai usar sempre

```bash
git checkout main
git pull
```

```bash
git fetch origin
git checkout nome-da-branch
```

```bash
git branch -a
```

---

## Três conselhos

**Revise cedo e em pedaços.** Quatro PRs chegando na véspera da reunião é o que mais trava o
grupo. Peça para as duplas abrirem o PR assim que tiverem o primeiro gráfico, mesmo incompleto.

**Não conserte o código da dupla você mesmo.** É tentador, mas tira o aprendizado. Comente o
que precisa mudar e deixe que eles mudem.

**Se uma dupla travar, o problema costuma ser a pergunta, não a pessoa.** Antes de ajudar com
código, confirme se está claro o que a pergunta pede.
