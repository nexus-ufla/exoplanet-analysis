# Roadmap do Projeto

Este documento mostra **onde o projeto quer chegar** e em que ponto estamos hoje.
Ninguém precisa dominar tudo isso agora — a ideia é ter um mapa. Avançamos uma fase
por vez, com calma, e cada fase só começa quando o grupo estiver confortável com a anterior.

## A visão (o objetivo final)

Construir um **classificador de trânsitos de exoplanetas**: um programa que olha o brilho
de uma estrela ao longo do tempo (uma "curva de luz") e decide se existe ali a assinatura
de um planeta passando na frente da estrela.

Quando um planeta cruza o disco da estrela, ele bloqueia um pouquinho da luz e o brilho
cai por algumas horas, de forma periódica. O detalhe é que esse sinal é **minúsculo**:
um planeta do tamanho da Terra em frente a uma estrela como o Sol bloqueia só ~0,008% da
luz (84 partes por milhão). Extrair isso do ruído é o coração do projeto.

A parte difícil não é achar quedas de brilho — é distinguir um **planeta de verdade** de
"impostores" (duas estrelas se eclipsando, manchas estelares, ruído do instrumento). Um
trânsito planetário tem fundo achatado (formato de "U"); uma binária de estrelas costuma
ter formato de "V" e um segundo eclipse. Toda a classificação mora nessa diferença de forma.

## As fases

| Fase | Foco | Situação |
| --- | --- | --- |
| **0 — EDA de catálogo** | Explorar as propriedades dos planetas já confirmados (raio, massa, período, temperatura da estrela) | **Estamos aqui** |
| **1 — Prova de conceito** | Baixar a curva de luz de UMA estrela conhecida (Kepler-10), limpar, achatar a tendência, achar o período e "dobrar" a curva até o trânsito aparecer | Futuro |
| **2 — Montar o dataset** | Baixar muitas curvas com o `lightkurve`, pegar os rótulos da tabela KOI e preparar os dados (com cuidado para separar treino/teste por estrela) | Futuro |
| **3 — Modelagem** | Um modelo simples com características físicas (Random Forest) e depois uma rede neural que aprende o formato do sinal | Futuro |
| **4 — Entrega** | Figuras finais, relatório, e talvez um app onde a pessoa digita o nome de uma estrela e vê a previsão | Futuro |

## O que estamos fazendo agora (Fase 0)

A Fase 0 é o nosso **aquecimento**. Trabalhamos com uma tabela de planetas já confirmados
(não com curvas de luz ainda) para:

- Praticar Python, pandas e gráficos.
- Aprender Git e trabalho em grupo.
- Entender as grandezas físicas (raio, massa, período orbital, temperatura da estrela) que
  vão importar nas próximas fases.

Quando estivermos confortáveis aqui, damos o próximo passo para a Fase 1.

## Termos que vão aparecer mais para frente

- **Curva de luz:** brilho da estrela medido ao longo do tempo.
- **Trânsito:** a queda de brilho quando o planeta passa na frente da estrela.
- **Detrending:** remover a variação lenta do brilho (da própria estrela e do instrumento)
  sem apagar o trânsito.
- **BLS (Box Least Squares):** algoritmo que procura a periodicidade do trânsito.
- **Phase folding:** sobrepor todos os ciclos para o trânsito "emergir" do ruído.
