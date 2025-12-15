#Resources
from flask_restful import Resource

from flask import make_response, render_template
# en este archivo estan los recursos que mi servidor tendra disponible
#ahora creearemos los recursos
#para nosotros poder crear recursos lo haremos atravez de clases y objetos
class HolaMundo(Resource):
    def get(self):
        return {'hola':'mundo'}

class PantallaInicio(Resource):
    def get(self):
        #renderizamos contenido del archivo html
        contenido = render_template('index.html')
        #retornamos el contenido renderizado en una respuesta
        return make_response(contenido)
#los recursos van a poder ejecutar dos acciones -> metodos