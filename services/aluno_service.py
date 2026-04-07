from domain.aluno import Aluno
from repositories.aluno_repository import aluno_repo

def criar_aluno(nome: str, email: str):
    
    if aluno_repo.buscar_por_email(email):
        raise ValueError("Já existe um aluno cadastrado com este e-mail.")
        
    novo_aluno = Aluno(nome=nome, email=email)
    return aluno_repo.salvar(novo_aluno)

def listar_alunos():
    return aluno_repo.listar_todos()