# To-do-List-Python

# Check List BD ✔️

Um gerenciador de tarefas simples feito em **Python + Tkinter**,
utilizando um banco de dados **SQLite (tarefas.db)** para armazenar
tarefas localmente. O objetivo do projeto é permitir que o usuário crie,
visualize, conclua e exclua tarefas em uma interface gráfica amigável.

## 📌 Funcionalidades

-   Adicionar novas tarefas
-   Listar tarefas existentes
-   Marcar como concluída
-   Excluir tarefas
-   Armazenamento em banco local SQLite
-   Interface gráfica construída com Tkinter

## 📁 Estrutura do Projeto

    chek_list_bd/
    │
    ├── banco.py
    ├── gerenciador.py
    ├── interface_tk.py
    ├── main.py
    ├── tarefa.py
    ├── tarefas.db
    └── README.md

## 🛠 Requisitos

-   Python 3.10+
-   Tkinter (padrão do Python)
-   Sem dependências externas

## 📥 Como Baixar o Projeto

### Clonar via Git

    git clone https://github.com/Henriquedacruz/To-do-List-Python.git

### Baixar ZIP

1.  Acesse o repositório no GitHub
2.  Clique em *Code*
3.  Clique em *Download ZIP*
4.  Extraia os arquivos

## ▶️ Como Executar Localmente

    python main.py

Ou clique duas vezes em `main.py`.

## 🗄 Sobre o Banco SQLite

O arquivo `tarefas.db` armazena: - ID da tarefa - Descrição - Status

Para resetar, basta deletar `tarefas.db`.

## 📝 Melhorias Futuras

-   Gerenciador não chamar funções direto do banco
-   Adicionar Try except
-   Gráfico de progresso
-   Cards diários 
