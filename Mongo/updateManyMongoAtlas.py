import pymongo
MONGO_BASEDATOS="datacenter"
MONGO_COLECCION="sistemas"

try:
    cliente = pymongo.MongoClient("mongodb+srv://pmurillo:748eVGxo3uMIckju@cluster-pruebas.3e85dfv.mongodb.net/?retryWrites=true&w=majority")
    cliente.server_info()
    print("Conexion a mongo exitosa")
    baseDatos=cliente[MONGO_BASEDATOS]
    coleccion=baseDatos[MONGO_COLECCION]
    #for documento in coleccion.find({"sensores.configuracion.temp_max":22},{"nombre":1,"sensores.configuracion.temp_max":1}):
    #    print(documento)
    coleccion.update_many({"tipo":"enfriamiento"},{"$set":{"actuadores.estado":True}})
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido ",errorTiempo)
