import uuid
from dataclasses import dataclass, field

@dataclass
class Aluno:
    nome: str
    email: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()), init=False)