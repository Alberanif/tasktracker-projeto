# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), escrito em Python 3.

Projeto do **Bootcamp II** (Engenharia de Software, Versionamento de Código e Desenvolvimento de Sistemas), Fase 2. A lógica implementada segue o planejamento da Fase 1, disponível em [`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

**Autor:** Alberani Gertrudes Filho, Ciência de Dados, polo Asa Norte.

## Funcionalidades

- Cadastrar tarefas com título, descrição, prioridade e data limite.
- Visualizar tarefas, com pendentes antes das concluídas e ordenação por prioridade e prazo.
- Concluir tarefas pelo ID.
- Mensagens claras para lista vazia e dados inválidos.

## Regras de negócio

| Regra | Descrição |
|---|---|
| R1 | O título é obrigatório. Entradas vazias ou só com espaços são rejeitadas. |
| R2 | A prioridade aceita apenas `Alta`, `Média` (ou `Media`) e `Baixa`. |
| R3 | A data limite deve estar em DD/MM/AAAA e não pode ser anterior a hoje. |
| R4 | Toda tarefa nasce com status `Pendente`. |
| R5 | Cada tarefa recebe um ID numérico único e crescente. |
| R6 | Só é possível concluir uma tarefa existente. |
| R7 | Na listagem, pendentes vêm antes das concluídas, por prioridade e depois por prazo. |

## Tecnologias

- Python 3.9 ou superior (somente biblioteca padrão)
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

```bash
git clone https://github.com/Alberanif/bootcamp.git
cd bootcamp
python src/main.py
```

Não há dependências externas para instalar.

## Uso

O programa exibe um menu que se repete até a escolha de **Sair**:

```
1 - Cadastrar tarefa
2 - Visualizar tarefas
3 - Concluir tarefa
4 - Sair
```

Os dados ficam apenas em memória e são perdidos ao encerrar o programa.

## Próximos passos

Fase 3: empacotamento, containerização com Docker, testes e deploy.
