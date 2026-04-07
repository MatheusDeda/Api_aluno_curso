from domain.curso import Curso
from typing import List, Optional

class CursoRepository:
    def __init__(self):
        
        self._cursos: List[Curso] = []

    def salvar(self, curso: Curso) -> Curso:
        """Adiciona um curso à nossa lista em memória."""
        self._cursos.append(curso)
        return curso

    def listar_todos(self) -> List[Curso]:
        """Retorna todos os cursos cadastrados."""
        return self._cursos

    def buscar_por_codigo(self, codigo: str) -> Optional[Curso]:
        """Busca um curso específico pelo código."""
        for curso in self._cursos:
            if curso.codigo == codigo:
                return curso
        return None

curso_repo = CursoRepository()