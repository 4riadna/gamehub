from flask import Flask, jsonify, request
from flasgger import Swagger
from database import get_connection

app = Flask(__name__)
Swagger(app, template_file='swagger.yaml')

@app.route('/')
def home():
    return "GameHub API funcionando"

@app.route('/productos', methods=['GET'])
def obtener_productos():

    conn = get_connection()

    productos = conn.execute(
        "SELECT * FROM videojuegos"
    ).fetchall()

    conn.close()

    return jsonify([dict(p) for p in productos])

@app.route('/carrito', methods=['GET'])
def ver_carrito():

    conn = get_connection()

    carrito = conn.execute("""
        SELECT
            c.id AS carrito_id,
            v.id AS videojuego_id,
            v.nombre,
            v.precio,
            v.genero,
            c.cantidad
        FROM carrito c
        JOIN videojuegos v
        ON c.videojuego_id = v.id
        WHERE c.fh_baja IS NULL
    """).fetchall()

    conn.close()

    return jsonify([dict(c) for c in carrito])

@app.route('/carrito/agregar', methods=['POST'])
def agregar_carrito():

    data = request.json
    producto_id = data.get("id")

    conn = get_connection()

    juego = conn.execute(
        "SELECT * FROM videojuegos WHERE id = ?",
        (producto_id,)
    ).fetchone()

    if not juego:
        conn.close()
        return jsonify({"error": "Producto no encontrado"}), 404

    conn.execute(
        """
        INSERT INTO carrito(videojuego_id)
        VALUES (?)
        """,
        (producto_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Producto agregado"})

@app.route('/carrito/eliminar/<int:id>', methods=['DELETE'])
def eliminar_carrito(id):

    conn = get_connection()

    conn.execute("""
        UPDATE carrito
        SET fh_baja = CURRENT_TIMESTAMP
        WHERE id = ?
        AND fh_baja IS NULL
    """, (id,))

    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Producto eliminado"})

@app.route('/carrito/total', methods=['GET'])
def total_carrito():

    conn = get_connection()

    total = conn.execute("""
        SELECT SUM(v.precio * c.cantidad)
        FROM carrito c
        JOIN videojuegos v
        ON c.videojuego_id = v.id
        WHERE c.fh_baja IS NULL
    """).fetchone()

    conn.close()

    return jsonify({
        "total": total[0] if total[0] else 0
    })

if __name__ == '__main__':
    app.run(debug=True)