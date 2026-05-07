from productos import productos
from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

carrito = []

@app.route('/')
def home():
    return "GameHub API funcionando"

@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

@app.route('/carrito', methods=['GET'])
def ver_carrito():
    return jsonify(carrito)

@app.route('/carrito/agregar', methods=['POST'])
def agregar_carrito():
    data = request.json
    producto_id = data.get("id")

    for producto in productos:
        if producto["id"] == producto_id:
            carrito.append(producto)
            return jsonify({"mensaje": "Producto agregado"})

    return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/carrito/eliminar/<int:id>', methods=['DELETE'])
def eliminar_carrito(id):
    global carrito
    carrito = [p for p in carrito if p["id"] != id]
    return jsonify({"mensaje": "Producto eliminado"})

@app.route('/carrito/total', methods=['GET'])
def total_carrito():
    total = sum(p["precio"] for p in carrito)
    return jsonify({"total": total})

if __name__ == '__main__':
    app.run(debug=True)