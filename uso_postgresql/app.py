from flask import Flask, jsonify, request
# Importacion de modulos externos
from dto.Flor_dto import Flor_dto
from dto.Flor_dto_m import Flor_schema
from modelos.FlorModel import FlorModel

app = Flask(__name__)

## generar la instancia de Flor
orquidea = Flor_dto("Vanda Paraguaya", "Violeta", "Vanda", "tipo1")
rosa = Flor_dto("Rosa blanca", "Blanca", "Rosa;L", "Rosaceae")
clavel = Flor_dto("Clavel", "Rosa eléctrico", "Dianthus", "Sweet William")
lista_flores = [orquidea, rosa, clavel]


@app.route("/traer_saludo", methods=['GET'])
def inicio():
    hola_diccionario = {
        "mensaje": "Hola",
        "estado": "este json esta purete"
    }
    return jsonify(hola_diccionario)

@app.route("/traer_flores")
def traerFlores():
    lista_enviar = []
    for flor in lista_flores:
        objeto = {}
        objeto["nombre"] = flor.nombre
        objeto["color"] = flor.color
        objeto["genero"] = flor.genero
        objeto["especie"] = flor.especie
        lista_enviar.append(objeto)

    return jsonify(lista_enviar)

@app.route('/traer_flores_m')
def traerFloresM():
    orquidea1 = Flor_dto("Phalaenosis", "Blanco", "Phalaenosis", "tipo1")
    orquidea2 = Flor_dto("Phalaenosis", "Atigrado", "Phalaenosis", "tipo1")
    schema = Flor_schema(many=True)
    resultado = schema.dump(lista_flores)
    print(resultado)
    return jsonify(resultado)

@app.route('/traer_flores_db')
def traerFloresDb():
    fm = FlorModel()
    return jsonify(fm.listarTodos())

@app.route('/nueva_flor', methods=["POST"])
def nuevaFlor():
    flor_recibida = request.json
    flor = Flor_dto(flor_recibida["nombre"], flor_recibida["color"], flor_recibida["genero"], flor_recibida["especie"])
    lista_flores.append(flor)
    print(flor_recibida)
    return "Exito"
 
## Aqui inicia el sistema
if __name__ == "__main__":    
    app.run(debug = True, port=3000)
