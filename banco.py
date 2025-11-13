import sqlite3
from tarefa import Tarefa

DB_NAME = "tarefas.db"

def inicializar_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        status TEXT DEFAULT 'Pendente'
    )''')
    conn.commit()
    conn.close()

def obter_tarefas():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, titulo, descricao, status FROM tarefas")
    rows = c.fetchall()
    conn.close()
    return [Tarefa(titulo, desc, status, id_) for (id_, titulo, desc, status) in rows]

def adicionar_tarefa(tarefa):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO tarefas (titulo, descricao, status) VALUES (?, ?, ?)",
              (tarefa.titulo, tarefa.descricao, tarefa.status))
    conn.commit()
    conn.close()

def atualizar_tarefa(tarefa_id, titulo, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE tarefas SET titulo=?, status=? WHERE id=?", (titulo, status, tarefa_id))
    conn.commit()
    conn.close()

def remover_tarefa(tarefa_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM tarefas WHERE id=?", (tarefa_id,))
    conn.commit()
    conn.close()
