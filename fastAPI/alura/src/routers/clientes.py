from fastapi import APIRouter

from schemas.clientes import Cliente

router = APIRouter(prefix='/clientes')

clients_list = [Cliente(id_=1, name='gabriel', telefone='123123', email='sfasdfa')]
              

@router.get('/', response_model=list[Cliente])
async def show_clients():

    return clients_list

@router.get('/{cliente_id}', response_model=Cliente | None)
async def show_clients_id(id_cliente:int):
    for client in clients_list: 
        if client.id_ == id_cliente:
            return client
        
    return None