# 🎮 GameHub

## Descripción

GameHub es una aplicación web SPA desarrollada como trabajo práctico de Programación Web 2.

La aplicación simula una tienda de videojuegos donde el usuario puede visualizar los productos disponibles, agregarlos al carrito, eliminarlos y calcular el total de la compra.

---

## Arquitectura

El proyecto está dividido en dos partes:

- **Frontend:** React
- **Backend:** Flask (Python)
- **Base de datos:** SQLite

El frontend consume una API REST desarrollada en Flask, que se comunica con una base de datos SQLite para gestionar los productos y el carrito de compras.

---

## Tecnologías utilizadas

### Backend
- Python
- Flask
- Flask-CORS
- SQLite
- Swagger (Flasgger)
- Pytest

### Frontend
- React
- Vite

### Testing
- Pytest (tests unitarios)
- Cypress (pruebas End-to-End)

---

## Funcionalidades

- Visualizar videojuegos disponibles.
- Agregar productos al carrito.
- Eliminar productos del carrito.
- Calcular el total de la compra.
- Persistencia de datos mediante SQLite.
- Documentación de la API con Swagger.
- Tests unitarios del backend.
- Pruebas End-to-End con Cypress.

---

## Endpoints principales

### Productos

- GET `/productos`

### Carrito

- GET `/carrito`
- POST `/carrito/agregar`
- DELETE `/carrito/eliminar/<id>`
- GET `/carrito/total`

---

## Pruebas

### Tests unitarios

Realizados con **Pytest** para validar los endpoints principales del backend.

### Pruebas E2E

Realizadas con **Cypress**, verificando:

- Flujo completo de compra.
- Persistencia de datos.
- Correcta interacción entre frontend y backend.
- Cálculo del total de la compra.

---

## Documentación

La API puede consultarse desde Swagger:

http://127.0.0.1:5000/apidocs

---

## Dificultades encontradas

Durante el desarrollo surgieron algunos desafíos:

- **Integración entre React y Flask:** al principio el frontend no podía comunicarse con el backend debido a la política CORS. Se resolvió configurando Flask-CORS.

---

## Ejecución del proyecto

1. Activar el entorno virtual

2. Ejecutar la aplicación:

```bash
python app.py
```

