from fastapi import APIRouter, HTTPException
from schemas.aluno_schema import AlunoCreate, AlunoResponse
from services import aluno_service

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("", response_model=AlunoResponse)
def post_aluno(aluno: AlunoCreate):
    try:
        return aluno_service.criar_aluno(nome=aluno.nome, email=aluno.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[AlunoResponse])
def get_alunos():
    return aluno_service.listar_alunos()