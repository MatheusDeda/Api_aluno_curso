API aluno e curso feito para matéria: Desenvolvimento rápido de aplicações em python

Agora vou orientar o passo a passo de como configurar o ambiente e executar o projeto em seu computador. 
Esse ponto é feito no programa pycharm ou vscode.

1º Clonar o repositório:
Abra seu cmd e digite git clone 

2º Acesse a pasta do projeto: 
cd nome-do-projeto

3º Crie o ambiente virtual (venv):
python -m venv venv

4º Ative o ambiente virtual (venv):
.\venv\Scripts\Activate.ps1

5º Ative o FastAPI e o Uvicorn:
pip install "fastapi[standard]"

6º Execulte a API: 
uvicorn main:app --reload

Esses passo a passo foram feitos no programa pycharm ou vscode.

Agora será feito no navegador (Edge, Chrome ou Firefox).
Com API rodando nos programas(pycharm, vscode), o FastAPI vai dar automaticamente uma documentação interativa para você.

PASSO A PASSO (navegador)

1º Abra o navegador de sua prferencia e acesse: http://127.0.0.1:8000/docs

2º Abrindo o navegador encontrará todas as rotas disponíveis (alunos, cursos).

3º Para testar o cadastro:

Clique na rota POST.

Clique em "Try it out".

Preencha o JSON e clique em "Execute".

O sistema gerará um ID (UUID) automático para o registro.

