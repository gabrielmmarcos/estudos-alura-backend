from pydantic import BaseModel

class Cliente (BaseModel):
    id_: int
    name: str
    email: str
    telefone: str