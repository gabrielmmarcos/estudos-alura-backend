from fastapi import FastAPI

from routers import clientes

app = FastAPI(
    title='teclog solutions',
    description='fazendo o crm basico para o curso da alura',
    version='1.0',
)

app.include_router(clientes.router)

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
