#Crear APIs y manejar exepciones
from datetime import date
from fastapi import FastAPI, HTTPException
#PAquete para trabajar con la estructura de los datos
from pydantic import BaseModel
#Conexion con MongoDB
from motor import motor_asyncio
from bson import ObjectId
#Configurar conexion con MongoDB
MONGO_URI="mongodb://localhost:27017" 
#Ejecutar el cliente de base de datos 
cliente=motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db=cliente["RESTful"] 
categorias_collection=db["categorias"]
clientes_collection=db["clientes"]
pedidos_collection=db["pedidos"]
productos_collection=db["productos"]

#Objeto para interactuar con la API
app = FastAPI()


#Modelo de datos para productos
class Productos(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int

#Modelo de datos para Categorías 
class Categorias(BaseModel): 
    id: int 
    nombre: str
    descripcion: str
    precio: float
    stock: int

#Modelo de datos para clientes
class Clientes(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo: str

#Modelo de datos para pedidos
class Pedidos(BaseModel):
    id: int
    fecha: date
    total: float
    productos: list[Productos]


# Modelo de actualizacion parcial

class UpdateProductoModel(BaseModel):
    id: int | None = None
    nombre: str | None = None
    descripcion: str | None = None
    precio: float | None = None
    stock: int | None = None

class UpdateCategoriaModel(BaseModel):
    id: int | None = None
    nombre: str | None = None
    descripcion: str | None = None
    precio: float | None = None
    stock: int | None = None

class UpdateClienteModel(BaseModel):
    id: int | None = None
    nombre: str | None = None
    apellido: str | None = None
    correo: str | None = None

class UpdatePedidoModel(BaseModel):
    id: int | None = None
    fecha: date | None = None
    total: float | None = None
    productos: list[Productos] | None = None







            ###METODOS GET
#Endpoint (ruta de url) para obtener productos DE LA DB 
@app.get("/productos/")
async def get_products():
    #Obtener de manera asincrona todos los usuarios
    resultados=dict() #tener todos los usuarios 
    productos=await productos_collection.find().to_list(None) 
    #Iterar todos los elementos de la lista users 
    for i, elemento in enumerate(productos): 
        resultados[i]=dict()
        resultados[i]["nombre"]=elemento["nombre"]
        resultados[i]["descripcion"]=elemento["descripcion"]
        resultados[i]["precio"]=elemento["precio"] 
        resultados[i]["stock"]=elemento["stock"] 
    return resultados


#Endpoint (ruta de url) para obtener categorias DE LA DB 
@app.get("/categorias/")
async def get_categorias():
    #Obtener de manera asincrona todos las categorias
    resultados=dict() #tener todos los usuarios 
    categorias=await categorias_collection.find().to_list(None) 
    #Iterar todos los elementos de la lista users 
    for i, elemento in enumerate(categorias): 
        resultados[i]=dict()
        resultados[i]["nombre"]=elemento["nombre"]
        resultados[i]["descripcion"]=elemento["descripcion"]
    return resultados

#Endpoint (ruta url) para obtener pedidos de la DB
@app.get("/pedidos/")
async def get_pedidos():
    #Obtener de manera asincrona todos los pedidos de la DB
    resultados = dict()
    pedidos = await pedidos_collection.find().to_list(None)
    #Iterar todos los elementos de la lista pedidos
    for i, elemento in enumerate(pedidos):
        resultados[i] = dict()
        resultados[i]["fecha"] = elemento["fecha"]
        resultados[i]["total"] = elemento["total"]
        resultados[i]["productos"] = elemento["productos"]
    return resultados 

#Endopint (ruta url) para obtener clientes de la DB
@app.get("/clientes/")
async def get_cliente():
    #Obtener de manera asincrona todos los clientes
    resultados = dict() #lista de clientes
    #Se guardan todos los clientes en una lista
    clientes = await clientes_collection.find().to_list(None)
    for i, elemento in enumerate(clientes):
        resultados[i] = dict()
        resultados[i]["nombre"] = elemento["nombre"]
        resultados[i]["apellido"] = elemento["apellido"]
        resultados[i]["correo"] = elemento["correo"]
    return resultados

        ##Metodos GET por id


# Obtener usuario por ID usando GET
@app.get("/clientes/{cliente_id}")
async def get_user_by_id(cliente_id: str):
    try:
        # Buscar el usuario por ObjectId
        cliente = await clientes_collection.find_one({"_id": ObjectId(cliente_id)})
        if not cliente:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")

    return {
        "nombre": cliente["nombre"],
        "apellido": cliente["apellido"],
        "correo": cliente["correo"]
    }

# Obtener prodcutos por ID usando GET
@app.get("/productos/{producto_id}")
async def get_producto_by_id(producto_id: str):
    try:
        # Buscar el producto por ObjectId
        producto = await productos_collection.find_one({"_id": ObjectId(producto_id)})
        if not producto:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")

    return {
        "nombre": producto["nombre"],
        "descripcion": producto["descripcion"],
        "precio": producto["precio"],
        "stock": producto["stock"]
    }

# Obtener categorias por ID usando GET
@app.get("/categorias/{cat_id}")
async def get_categoria_by_id(cat_id: str):
    try:
        # Buscar el producto por ObjectId
        categoria = await categorias_collection.find_one({"_id": ObjectId(cat_id)})
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria no encontrado")
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")

    return {
        "nombre": categoria["nombre"],
        "descripcion": categoria["descripcion"]
    }

# Obtener pedidos por ID usando GET
@app.get("/pedidos/{pedido_id}")
async def get_prodido_by_id(pedido_id: str):
    try:
        # Buscar el producto por ObjectId
        pedido = await pedidos_collection.find_one({"_id": ObjectId(pedido_id)})
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")

    return {
        "fecha": pedido["fecha"],
        "total": pedido["total"],
        "productos": pedido["productos"],
        
    }


#METODOS POST
#Metodo para agregar productos a la DB
@app.post("/productos/")
async def create_producto(producto: Productos): 
    #se agrega un producto a la base de datos
    #Los datos del producto deben estar en diccionario 
    await productos_collection.insert_one(producto.dict()) 
    return{
        "message":"El producto se agrego correctamente"
    }

#Metodo para agregar pedidos a la DB
@app.post("/pedidos/")
async def create_pedido(pedido: Pedidos):
    #Se agrega un pedido a la DB
    await pedidos_collection.insert_one(pedido.dict())
    return {
        "message": "El pedido se agrego correctamente"
    }

#Metodo para agregar categorias a la DB
@app.post("/categorias/")
async def create_categoria(categoria: Categorias):
    #Agregar categoria a pedido a la DB
    await pedidos_collection.insert_one(categoria.dict())
    return {
        "message":"Se agrego la categoria correctamente"
    }
#Metodo para agregar clientes a la DB
@app.post("/clientes/")
async def create_cliente(cliente: Clientes):
    #Agregar cliente a la DB
    await clientes_collection.insert_one(cliente.dict())
    return {
        "message":"Se agrego el cliente correctamente"
    }

                #Metodos Update
                #Metodos Delete

#Eliminar productos por ID
@app.delete("/productos/{producto_id}")
async def delete_producto_id(producto_id: str):
    try:
        resultado = await productos_collection.delete_one({"_id":ObjectId(producto_id)})

    except Exception as e:
        raise HTTPException(status_code=404, detail="Formato inválido por el ID del producto")
    if resultado.deleted_count==0:
        raise HTTPException(status_code=404,detail="Producto no encontrado")
    return{
        "message": "Producto eliminado correctamente"
        }

#Eliminar categorias por ID
@app.delete("/categorias/{categoria_id}")
async def delete_categoria_id(categoria_id: str):
    try: 
        resultado = await categorias_collection.delete_one({"_id":ObjectId(categoria_id)})
    except Exception as e:
        raise HTTPException(status_code=404, detail="Formato invalido")
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {
        "message":"Categoria eliminada correctamente"
    }

#Eliminar pedidos por ID
@app.delete("/pedidos/{pedido_id}")
async def delete_pedido_id(pedido_id: str):
    try:
        resultado = await pedidos_collection.delete_one({"_id":ObjectId(pedido_id)})
    except Exception as e:
        raise HTTPException(status_code=404, detail="Codigo invalido")
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return {
        "message": "Pedido eliminado correctamente"
    }

#Eliminar cliente por ID
@app.delete("/clientes/{cliente_id}")
async def delete_cliente_id(cliente_id: str):
    try:
        resultado = await clientes_collection.delete_one({"_id":ObjectId(cliente_id)})
    except Exception as e:
        raise HTTPException(status_code=404, detail="Codigo invalido")
    if resultado.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return {
        "message": "Cliente eliminado correctamente"
    }

#Metodos UPDATE

# Actualizar usuario por ObjectId
@app.put("/clientes/{cliente_id}")
async def update_user(cliente_id: str, client_data: UpdateClienteModel):
    try:
        # Crear el filtro con ObjectId
        filtro = {"_id": ObjectId(cliente_id)}
        
        # Crear el diccionario de actualización
        actualizacion = {k: v for k, v in client_data.dict().items() if v is not None}
        
        if not actualizacion:
            raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")
        
        # Realizar la actualización
        resultado = await clientes_collection.update_one(filtro, {"$set": actualizacion})
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")
    
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o no modificado")
    
    return {"message": "Usuario actualizado correctamente"}

# Actualizar producto por ObjectId
@app.put("/productos/{producto_id}")
async def update_producto(producto_id: str, product_data: UpdateProductoModel):
    try:
        # Crear el filtro con ObjectId
        filtro = {"_id": ObjectId(producto_id)}
        
        # Crear el diccionario de actualización
        actualizacion = {k: v for k, v in product_data.dict().items() if v is not None}
        
        if not actualizacion:
            raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")
        
        # Realizar la actualización
        resultado = await productos_collection.update_one(filtro, {"$set": actualizacion})
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")
    
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Producto no encontrado o no modificado")
    
    return {"message": "Producto actualizado correctamente"}

# Actualizar categoria por ObjectId
@app.put("/categorias/{categoria_id}")
async def update_producto(categoria_id: str, cat_data: UpdateCategoriaModel):
    try:
        # Crear el filtro con ObjectId
        filtro = {"_id": ObjectId(categoria_id)}
        
        # Crear el diccionario de actualización
        actualizacion = {k: v for k, v in cat_data.dict().items() if v is not None}
        
        if not actualizacion:
            raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")
        
        # Realizar la actualización
        resultado = await categorias_collection.update_one(filtro, {"$set": actualizacion})
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")
    
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Categoria no encontrado o no modificado")
    
    return {"message": "Categoria actualizado correctamente"}



# Actualizar Pedido por ObjectId
@app.put("/pedidos/{pedido_id}")
async def update_pedidos(pedido_id: str, ped_data: UpdatePedidoModel):
    try:
        # Crear el filtro con ObjectId
        filtro = {"_id": ObjectId(pedido_id)}
        
        # Crear el diccionario de actualización
        actualizacion = {k: v for k, v in ped_data.dict().items() if v is not None}
        
        if not actualizacion:
            raise HTTPException(status_code=400, detail="No se proporcionaron datos para actualizar")
        
        # Realizar la actualización
        resultado = await pedidos_collection.update_one(filtro, {"$set": actualizacion})
    except Exception:
        raise HTTPException(status_code=400, detail="Formato inválido del ID")
    
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Pedido no encontrado o no modificado")
    
    return {"message": "Pedido actualizado correctamente"}