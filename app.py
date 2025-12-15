#desde la libreria flask
#vamos a importar la clase flask
from flask import Flask
#desde la libreria flask_restful importamos la clase API y la clase Resource
from flask_restful import Api, Resource
from rutas import crear_rutas

#vamos a crear un objeto de tipo Flask
app= Flask(__name__)

#creamos un objto de tipo API, y como argumento le pasamos el objeto app
api = Api(app)
# la api sera el programa que se comunique con el dispositivo fisico
crear_rutas(api)
# del objeto app ejecutamos el metodo run
app.run(port=8080,debug=True)





