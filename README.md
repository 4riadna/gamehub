# GameHub Backend API

## Descripción
GameHub es una API REST desarrollada con Flask que simula un sistema de carrito de compras de videojuegos. Este proyecto corresponde a la Etapa 1 del trabajo práctico de Programación Web 2.

La aplicación permite gestionar productos, agregarlos al carrito y calcular el total de la compra.

---

## Tecnologías utilizadas
- Python
- Flask
- Pytest
- Flasgger (Swagger)
- Git / GitHub

---

## Funcionalidades principales

- Listar productos disponibles
- Filtrar productos por género
- Agregar productos al carrito
- Eliminar productos del carrito
- Calcular el total de la compra

---

## Endpoints de la API

### Productos
- GET `/productos`
- GET `/productos?genero=indie`

### Carrito
- GET `/carrito`
- POST `/carrito/agregar`
- DELETE `/carrito/eliminar/<id>`
- GET `/carrito/total`

---

## Ejecución del proyecto

Instalar dependencias:
pip install -r requirements.txt

Ejecutar la aplicación:
python app.py

---

## Tests

Ejecutar tests con:
pytest

---

## Documentación

La API está documentada con Swagger:

http://127.0.0.1:5000/apidocs