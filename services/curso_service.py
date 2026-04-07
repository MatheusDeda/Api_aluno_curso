from domain.curso import Curso
from repositories.curso_repository import curso_repo

def criar_curso(codigo: str, titulo: str, preco: float, tipo: int, desconto_percentual: float = 0.0):
    # 1. Verifica se o curso já existe
    if curso_repo.buscar_por_codigo(codigo):
        raise ValueError(f"Curso com código {codigo} já existe.")
    
    # 2. Cria o objeto de domínio 
    novo_curso = Curso(
        codigo=codigo,
        titulo=titulo,
        preco=preco,
        tipo=tipo,
        desconto_percentual=desconto_percentual
    )
    
    # 3. Salva no repositório
    return curso_repo.salvar(novo_curso)

def listar_cursos():
    return curso_repo.listar_todos()

def buscar_curso(codigo: str):
    curso = curso_repo.buscar_por_codigo(codigo)
    if not curso:
        raise ValueError("Curso não encontrado.")
    return curso

def atualizar_preco(codigo: str, novo_preco: float):
    # Busca o curso existente.
    curso = buscar_curso(codigo)
    
    # Atualiza o valor.
    curso.preco = novo_preco
    
    # já atualizado na lista, porém retornamos para confirmar.
    return curso