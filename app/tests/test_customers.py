from fastapi import status

"""
El cliente (client) que se utiliza en los tests proviene de la dependencia 
gestionada por pytest en forma de un fixture. Aunque no se importa 
explícitamente en el archivo, pytest lo resuelve automáticamente 
porque está definido como un @pytest.fixture en otro lugar del proyecto.
"""
def test_create_customer(client):
    response = client.post(
        "/customers",
        json={
            "name": "Jhon Doe",
            "email": "jhon@example.com",
            "age": 33,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_read_customer(client):
    response = client.post(
        "/customers",
        json={
            "name": "Jhon Doe",
            "email": "jhon@example.com",
            "age": 33,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id: int = response.json()["id"]
    response_read = client.get(f"/customers/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    assert response_read.json()["name"] == "Jhon Doe"
    
def test_read_all_customers(client):
    response = client.get("/customers")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == []