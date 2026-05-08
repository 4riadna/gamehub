from app import app

def test_obtener_productos():
    client = app.test_client()
    response = client.get('/productos')
    assert response.status_code == 200

def test_agregar_carrito():
    client = app.test_client()
    response = client.post('/carrito/agregar', json={"id": 1})
    assert response.status_code == 200

def test_total_carrito():
    client = app.test_client()
    client.post('/carrito/agregar', json={"id": 1})
    response = client.get('/carrito/total')
    assert response.status_code == 200

def test_eliminar_carrito():
    client = app.test_client()

    client.post('/carrito/agregar', json={"id": 1})

    response = client.delete('/carrito/eliminar/1')

    assert response.status_code == 200