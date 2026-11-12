# Catálogo de Productos Tecnológicos - Django MTV

Aplicación web desarrollada en Django aplicando el patrón arquitectónico Model-Template-View (MTV), enrutamiento modular, vistas basadas en funciones (FBV) y clases (CBV), herencia de plantillas y consultas ORM sobre SQLite.

## Diagrama de Flujo MTV


[Cliente / Navegador]
         │
         ▼  1. HTTP Request (GET /catalogo/)
   [config/urls.py] ──▶ [catalogo/urls.py]
         │
         ▼  2. Despacha a ProductoListView (CBV)
  [catalogo/views.py]
         │
         ▼  3. Consulta QuerySet filtrado
  [catalogo/models.py] ◀──▶ [SQLite DB]
         │
         ▼  4. Inyecta contexto (productos)
[templates/catalogo.html] ──▶ Hereda de [templates/base.html]
         │
         ▼  5. HTTP Response (HTML renderizado)
[Cliente / Navegador]
