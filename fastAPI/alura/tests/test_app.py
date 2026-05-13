from http import HTTPStatus

from fastapi.testclient import TestClient

from src.alura.app import app


def testando_print():
    cliente = TestClient(app)

    response = cliente.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}
