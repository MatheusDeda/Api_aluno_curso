import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from api.aluno import router as aluno_router
from api.curso import router as curso_router

app = FastAPI(title="Sistema Escolar API")

app.include_router(aluno_router)
app.include_router(curso_router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à API do Matheus!"}