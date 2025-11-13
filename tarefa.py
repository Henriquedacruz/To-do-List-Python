class Tarefa:
    def __init__(self, titulo, descricao, status="Pendente", id=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            titulo=data["titulo"],
            descricao=data.get("descricao", ""),
            status=data.get("status", "Pendente"),
            id=data.get("id")
        )
