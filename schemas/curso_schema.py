from pydantic import BaseModel, Field
from typing import Optional

# SCHEMA DE ENTRADA 

class CursoCreate(BaseModel):
    codigo: str
    titulo: str
    preco: float = Field(..., ge=0.0, description="Preço base do curso. Não pode ser negativo.")
    tipo: int = Field(..., description="1 para Gratuito, 2 para Pago")
    desconto_percentual: Optional[float] = Field(default=0.0, ge=0.0)


# SCHEMA DE SAÍDA 

class CursoResponse(BaseModel):
    codigo: str
    titulo: str
    preco: float
    tipo: int
    desconto_percentual: float
    preco_final: float  

    class Config:
        from_attributes = True