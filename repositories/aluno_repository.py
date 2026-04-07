from domain.aluno import Aluno
from typing import List, Optional

class AlunoRepository:
    def __init__(self):
        # Lista que simula a tabela de alunos
        self._alunos: List[Aluno] = []

    def salvar(self, aluno: Aluno) -> Aluno:
        """Adiciona um aluno à lista."""
        self._alunos.append(aluno)
        return aluno

    def listar_todos(self) -> List[Aluno]:
        """Retorna todos os alunos cadastrados."""
        return self._alunos

    def buscar_por_email(self, email: str) -> Optional[Aluno]:
        """Busca um aluno pelo e-mail (geralmente um campo único)."""
        for aluno in self._alunos:
            if aluno.email == email:
                return aluno
        return None

#instaciamos uma global
aluno_repo = AlunoRepository()