import customtkinter as ctk
from tarefa import Tarefa
from gerenciador import Gerenciador

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.g = Gerenciador()
        self.title("To-Do List Moderna")
        self.geometry("600x500")
        self.configure(padx=20, pady=20)

        # Entrada de tarefa
        self.entry = ctk.CTkEntry(self, placeholder_text="Digite a tarefa")
        self.entry.pack(fill="x", pady=10)

        self.button_add = ctk.CTkButton(self, text="Adicionar", command=self.adicionar)
        self.button_add.pack(pady=5)

        # Lista de tarefas
        self.listbox = ctk.CTkScrollableFrame(self, width=550, height=300)
        self.listbox.pack(fill="both", expand=True, pady=10)

        # Modo escuro/claro
        self.switch_mode = ctk.CTkSwitch(self, text="Modo Escuro", command=self.toggle_mode)
        self.switch_mode.select()
        self.switch_mode.pack(pady=5)

        self.atualizar_lista()

    def toggle_mode(self):
        if self.switch_mode.get():
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def adicionar(self):
        titulo = self.entry.get()
        if titulo:
            self.g.adicionar(Tarefa(titulo, ""))
            self.entry.delete(0, 'end')
            self.atualizar_lista()

    def atualizar_lista(self):
        for widget in self.listbox.winfo_children():
            widget.destroy()

        for index, tarefa in enumerate(self.g.tarefas):
            frame = ctk.CTkFrame(self.listbox, fg_color="transparent")
            frame.pack(fill="x", pady=5)

            status_text = "✅ " if tarefa.status == "Concluída" else ""
            label = ctk.CTkLabel(frame, text=f"{status_text}{tarefa.titulo}", anchor="w")
            label.pack(side="left", expand=True)

            # Botões de ação
            ctk.CTkButton(frame, text="✓", width=30,
                          command=lambda i=index: self.marcar(i)).pack(side="left", padx=2)
            ctk.CTkButton(frame, text="✎", width=30,
                          command=lambda i=index: self.editar(i)).pack(side="left", padx=2)
            ctk.CTkButton(frame, text="🗑", width=30,
                          command=lambda i=index: self.remover(i)).pack(side="left", padx=2)
            ctk.CTkButton(frame, text="↑", width=30,
                          command=lambda i=index: self.mover(i, -1)).pack(side="left", padx=2)
            ctk.CTkButton(frame, text="↓", width=30,
                          command=lambda i=index: self.mover(i, 1)).pack(side="left", padx=2)

    def marcar(self, index):
        tarefa = self.g.tarefas[index]
        tarefa.status = "Concluída" if tarefa.status != "Concluída" else "Pendente"
        self.g.atualizar(tarefa)
        self.atualizar_lista()

    def editar(self, index):
        tarefa = self.g.tarefas[index]
        nova = ctk.CTkInputDialog(title="Editar Tarefa", text="Novo título:")
        novo_texto = nova.get_input()
        if novo_texto:
            tarefa.titulo = novo_texto
            self.g.atualizar(tarefa)
            self.atualizar_lista()

    def remover(self, index):
        self.g.remover(index + 1)
        self.atualizar_lista()

    def mover(self, index, direcao):
        nova_pos = index + direcao
        if 0 <= nova_pos < len(self.g.tarefas):
            self.g.tarefas[index], self.g.tarefas[nova_pos] = self.g.tarefas[nova_pos], self.g.tarefas[index]
            
            self.atualizar_lista()

if __name__ == "__main__":
    app = App()
    app.mainloop()
