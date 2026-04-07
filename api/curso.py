from fastapi import APIRouter, HTTPException
from schemas.curso_schema import CursoCreate, CursoResponse
from services import curso_service

router = APIRouter(prefix="/cursos", tags=["Cursos"])

@router.post("", response_model=CursoResponse)
def post_curso(curso: CursoCreate):
    try:
        return curso_service.criar_curso(
            codigo=curso.codigo,
            titulo=curso.titulo,
            preco=curso.preco,
            tipo=curso.tipo,
            desconto_percentual=curso.desconto_percentual
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("", response_model=list[CursoResponse])
def get_cursos():
    return curso_service.listar_cursos()

@router.get("/{codigo}", response_model=CursoResponse)
def get_curso_por_codigo(codigo: str):
    try:
        return curso_service.buscar_curso(codigo)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{codigo}/preco", response_model=CursoResponse)
def put_atualizar_preco(codigo: str, novo_preco: float):
    try:
        # Note: novo_preco aqui vem como Query Parameter ou você pode criar um mini schema
        return curso_service.atualizar_preco(codigo, novo_preco)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{codigo}/preco-final")
def get_preco_final(codigo: str):
    try:
        curso = curso_service.buscar_curso(codigo)
        return {"codigo": codigo, "preco_final": curso.preco_final}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))