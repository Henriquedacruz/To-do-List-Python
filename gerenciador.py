from banco import obter_tarefas, adicionar_tarefa, atualizar_tarefa, remover_tarefa
from tarefa import Tarefa

class Gerenciador:
    def __init__(self):
        self.tarefas = obter_tarefas()

    def adicionar(self, tarefa: Tarefa):
        adicionar_tarefa(tarefa)
        self.tarefas = obter_tarefas()

    def atualizar(self, tarefa: Tarefa):
        if tarefa.id is not None:
            atualizar_tarefa(tarefa.id, tarefa.titulo, tarefa.status)
            self.tarefas = obter_tarefas()

    def remover(self, tarefa_id: int):
        if 0 < tarefa_id <= len(self.tarefas):
            tarefa = self.tarefas[tarefa_id - 1]
            remover_tarefa(tarefa.id)
            self.tarefas = obter_tarefas()


    def salvar(self):
        # compatibilidade com código antigo — apenas recarrega as tarefas
        self.tarefas = obter_tarefas()
