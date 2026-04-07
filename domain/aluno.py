import uuid #gera automaticamente
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum

@dataclass
class Aluno:
    nome: str
    email: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)

    def __init__(self, nome: str, email: str, id: str):
        self.nome = nome
        self.email = email
        self.id = id

        print(f"Objeto Aluno criado para: {self.nome}")
        print(f"Objeto email criado para: {self.email}")
        

novo_aluno = Aluno (nome="matheus", email="matheus@gmail.com", id= "")
print(novo_aluno)
