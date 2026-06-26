import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [productos, setProductos] = useState([]);
  const [carrito, setCarrito] = useState([]);
  const [total, setTotal] = useState(0);
  const [mensaje, setMensaje] = useState("");
  const [agregado, setAgregado] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/productos")
      .then((res) => res.json())
      .then((data) => setProductos(data));

    cargarCarrito();
  }, []);

  function cargarCarrito() {
    fetch("http://127.0.0.1:5000/carrito")
      .then((res) => res.json())
      .then((data) => setCarrito(data));

    fetch("http://127.0.0.1:5000/carrito/total")
      .then((res) => res.json())
      .then((data) => setTotal(data.total));
  }

  function agregarAlCarrito(id) {
    fetch("http://127.0.0.1:5000/carrito/agregar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ id }),
    })
      .then((res) => res.json())
      .then(() => {
        cargarCarrito();

        setAgregado(id);

        setTimeout(() => {
          setAgregado(null);
        }, 1000);
      });
  }

  function eliminarDelCarrito(id) {
    fetch(`http://127.0.0.1:5000/carrito/eliminar/${id}`, {
      method: "DELETE",
    })
      .then((res) => res.json())
      .then(() => {
        setMensaje("🗑️ Producto eliminado del carrito.");

        cargarCarrito();

        setTimeout(() => {
          setMensaje("");
        }, 2000);
      });
  }

    return (
  <div className="container">

    <nav className="navbar">
      <a href="#productos">Productos</a>
      <a href="#carrito">Carrito</a>
    </nav>

    <header className="hero">
      <div className="hero-content">
        <h1>🎮 GameHub</h1>

        <p>
          Descubrí nuevos mundos, armá tu colección y encontrá tus juegos favoritos.
        </p>
      </div>
    </header>

    <h2 id="productos">Videojuegos</h2>
    <p>Total de juegos: {productos.length}</p>

    <div className="juegos">
      {productos.map((juego) => (
        <div className="card" key={juego.id}>
          <h3>{juego.nombre}</h3>

          <p>Género: {juego.genero}</p>

          <p>Precio: ${juego.precio}</p>

          <button onClick={() => agregarAlCarrito(juego.id)}
            disabled={agregado === juego.id}
            className={agregado === juego.id ? "agregado" : ""}>
            {agregado === juego.id ? "✓ Agregado" : "Agregar al carrito"}
          </button>
        </div>
      ))}
    </div>

    <div className="carrito">
      <h2 id="carrito">🛒 Carrito</h2>
      {mensaje && <div className="mensaje">{mensaje}</div>}
      <p>Productos en el carrito: {carrito.length}</p>

      {carrito.length === 0 ? (
        <p>El carrito está vacío.</p>
      ) : (
        carrito.map((item) => (
          <div className="item-carrito" key={item.carrito_id}>
            <h3>{item.nombre}</h3>

            <p>Precio: ${item.precio}</p>

            <p>Cantidad: {item.cantidad}</p>

            <button onClick={() => eliminarDelCarrito(item.carrito_id)}>
              Eliminar
            </button>
          </div>
        ))
      )}

      <h2 className="total">Total: ${total}</h2>
    </div>
  </div>
);
}

export default App;