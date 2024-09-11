API RESTful para Tienda en Línea
## Descripción:
Este proyecto consiste en la creación de una API RESTful para una tienda en línea, utilizando FastAPI y MongoDB como base de datos. La API permite gestionar varias colecciones que almacenan información sobre productos, categorías, pedidos y clientes. Se implementan las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para cada una de las colecciones.

## Objetivos:
Diseñar y crear varias colecciones en MongoDB para almacenar datos de una tienda en línea.
Implementar una API RESTful que permita interactuar con las colecciones de MongoDB.
Consumir la API desde un cliente HTTP para probar su funcionalidad.

## Colecciones:
1. Productos
id (ObjectId): identificador único del producto.
nombre (String): nombre del producto.
descripción (String): descripción del producto.
precio (Number): precio del producto.
stock (Number): cantidad de unidades en stock.


2. Categorías
id (ObjectId): identificador único de la categoría.
nombre (String): nombre de la categoría.
descripción (String): descripción de la categoría.


3. Pedidos
id (ObjectId): identificador único del pedido.
fecha (Date): fecha en que se realizó el pedido.
total (Number): total del pedido.
productos (Array): arreglo de productos incluidos en el pedido.


4. Clientes
id (ObjectId): identificador único del cliente.
nombre (String): nombre del cliente.
apellido (String): apellido del cliente.
correo electrónico (String): correo electrónico del cliente.

## Endpoints de la API
Para cada una de las colecciones mencionadas, la API proporciona los siguientes endpoints:

Productos:
GET /productos/: Obtener todos los productos.
GET /productos/{id}: Obtener un producto por su ID.
POST /productos/: Crear un nuevo producto.
PUT /productos/{id}: Actualizar un producto existente.
DELETE /productos/{id}: Eliminar un producto por su ID.

Categorías:
GET /categorias/: Obtener todas las categorías.
GET /categorias/{id}: Obtener una categoría por su ID.
POST /categorias/: Crear una nueva categoría.
PUT /categorias/{id}: Actualizar una categoría existente.
DELETE /categorias/{id}: Eliminar una categoría por su ID.

Pedidos:
GET /pedidos/: Obtener todos los pedidos.
GET /pedidos/{id}: Obtener un pedido por su ID.
POST /pedidos/: Crear un nuevo pedido.
PUT /pedidos/{id}: Actualizar un pedido existente.
DELETE /pedidos/{id}: Eliminar un pedido por su ID.

Clientes:
GET /clientes/: Obtener todos los clientes.
GET /clientes/{id}: Obtener un cliente por su ID.
POST /clientes/: Crear un nuevo cliente.
PUT /clientes/{id}: Actualizar un cliente existente.
DELETE /clientes/{id}: Eliminar un cliente por su ID.


## Tecnologías Utilizadas
- **FastAPI**: Framework para crear APIs rápidas y eficientes.
- **Motor**: Cliente asíncrono para MongoDB.
- **MongoDB**: Base de datos NoSQL utilizada para almacenar los datos de la tienda.


Puedes instalar las dependencias ejecutando:
$ pip install "fastapi[standard]"


## Pruebas
Puedes probar la API utilizando Postman, cURL o cualquier cliente HTTP. También puedes acceder a la documentación automática generada por FastAPI en la ruta /docs para probar los diferentes endpoints directamente desde tu navegador.

