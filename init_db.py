import sqlite3

conn = sqlite3.connect("gamehub.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS videojuegos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    genero TEXT NOT NULL,
    fh_baja DATETIME DEFAULT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS carrito(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    videojuego_id INTEGER NOT NULL,
    cantidad INTEGER DEFAULT 1,
    fh_baja DATETIME DEFAULT NULL,
    FOREIGN KEY(videojuego_id)
    REFERENCES videojuegos(id)
)
""")

juegos = [
    ("Devil May Cry 5", 4000, "Accion"),
    ("Uncharted 4", 4200, "Aventura"),
    ("Call of Duty", 12000, "Accion"),
    ("Resident Evil 4", 4800, "Horror"),
    ("Assassin's Creed II", 3500, "Aventura"),
    ("Elden Ring", 15000, "RPG"),
    ("Dark Souls III", 12000, "RPG"),
    ("Sekiro", 13000, "Accion"),
    ("Cyberpunk 2077", 12000, "RPG"),
    ("The Witcher 3", 10000, "RPG")
]

cursor.executemany("""
INSERT INTO videojuegos(nombre, precio, genero)
VALUES (?, ?, ?)
""", juegos)

conn.commit()
conn.close()

print("Base creada")