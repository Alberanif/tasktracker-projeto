"""TaskTracker - gerenciador de tarefas em linha de comando (Bootcamp II, Fase 2)."""

MENU = """
===== TASKTRACKER =====
1 - Cadastrar tarefa
2 - Visualizar tarefas
3 - Concluir tarefa
4 - Sair
"""


def cadastrar_tarefa(tarefas, proximo_id):
    """Cadastra uma tarefa e devolve o próximo ID disponível."""
    titulo = input("Título: ")
    descricao = input("Descrição (opcional): ")
    prioridade = input("Prioridade (Alta, Média ou Baixa): ")
    data_limite = input("Data limite (DD/MM/AAAA): ")

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
