#las rutas de acceso a cada recursos
from recursos import *
#tener el objeto API
def crear_rutas(api):
    # quiero que puedas acceder a este recurdo por medio de tal ruta
    # 1-.el recurso que va ejecutar
    # 2-. la direccion de este recurso
    api.add_resource(HolaMundo, '/hola')
    # La ruta de inicio
    api.add_resource(PantallaInicio, '/')




