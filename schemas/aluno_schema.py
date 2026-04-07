from pydantic import BaseModel, Field

class AlunoCreate(BaseModel):
    nome: str
    email: str

class AlunoResponse(BaseModel): 
    nome: str
    email: str

    class Config:
        from_attributes = True