describe("GameHub - Pruebas E2E", () => {

  const juego = "Devil May Cry 5";

  beforeEach(() => {
    cy.visit("http://localhost:5173");
  });

  it("Flujo de compra completo", () => {

    // Verifica que la página cargó correctamente
    cy.contains("Videojuegos");

    // Agrega un producto al carrito
    cy.contains(juego)
      .parent()
      .contains("Agregar al carrito")
      .click();

    // Va al carrito
    cy.contains("Carrito").click();

    // Comprueba que el producto aparece en el carrito
    cy.get(".carrito")
      .should("contain", juego);

    // Comprueba que existe el botón eliminar
    cy.get(".carrito")
      .contains("Eliminar")
      .should("exist");

    // Elimina el primer producto
    cy.get(".carrito")
      .contains("Eliminar")
      .first()
      .click();

  });


  it("Persistencia de datos", () => {

    // Agrega un producto
    cy.contains(juego)
      .parent()
      .contains("Agregar al carrito")
      .click();

    // Recarga la página
    cy.reload();

    // Va al carrito
    cy.contains("Carrito").click();

    // El producto sigue existiendo
    cy.get(".carrito")
      .should("contain", juego);

  });

  it("Correcta interacción entre frontend y backend", () => {

  // Intercepta la petición al backend
  cy.intercept("GET", "http://127.0.0.1:5000/productos").as("productos");

  cy.visit("http://localhost:5173");

  // Espera la respuesta del backend
  cy.wait("@productos")
    .its("response.statusCode")
    .should("eq", 200);

  // Comprueba que React mostró los productos recibidos
  cy.contains("Videojuegos");
  cy.contains("Devil May Cry 5");

  });


  it("Calcula el total de la compra", () => {

    cy.contains(juego)
      .parent()
      .contains("Agregar al carrito")
      .click();

    cy.get(".total")
      .should("contain", "Total:");

  });

});