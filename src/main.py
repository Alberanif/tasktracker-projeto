"""TaskTracker - gerenciador de tarefas em linha de comando (Bootcamp II, Fase 2)."""

from datetime import date, datetime

MENU = """
===== TASKTRACKER =====
1 - Cadastrar tarefa
2 - Visualizar tarefas
3 - Concluir tarefa
4 - Sair
"""


PRIORIDADES = {"alta": "Alta", "média": "Média", "media": "Média", "baixa": "Baixa"}


def ler_titulo():
    """R1: repete o prompt até receber um título não vazio."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("Erro: o título é obrigatório e não pode ficar vazio.")


def ler_prioridade():
    """R2: aceita somente Alta, Média (ou Media) e Baixa."""
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES:
            return PRIORIDADES[entrada]
        print("Erro: prioridade inválida. Use Alta, Média ou Baixa.")


def ler_data_limite():
    """R3: exige DD/MM/AAAA válida e não anterior à data atual."""
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y").date()
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA.")
            continue
        if data < date.today():
            print("Erro: a data limite não pode ser anterior a hoje.")
            continue
        return entrada


def cadastrar_tarefa(tarefas, proximo_id):
    """Cadastra uma tarefa e devolve o próximo ID disponível."""
    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()

    tarefas.append({
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    })
    print(f"Tarefa cadastrada com sucesso! ID: {proximo_id}")
    return proximo_id + 1


def visualizar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas."""
    if not tarefas:
        print("Ainda não existem tarefas cadastradas.")
        return

    for tarefa in tarefas:
        print(f"\n[{tarefa['id']}] {tarefa['titulo']}")
        print(f"    Descrição : {tarefa['descricao']}")
        print(f"    Prioridade: {tarefa['prioridade']}")
        print(f"    Data limite: {tarefa['data_limite']}")
        print(f"    Status    : {tarefa['status']}")


def main():
    tarefas = []
    proximo_id = 1

    while True:
        print(MENU)
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            proximo_id = cadastrar_tarefa(tarefas, proximo_id)
        elif opcao == "2":
            visualizar_tarefas(tarefas)
        elif opcao == "3":
            print("Funcionalidade ainda não implementada.")
        elif opcao == "4":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 4.")


if __name__ == "__main__":
    main()
