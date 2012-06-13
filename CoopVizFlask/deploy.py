import os

from progressbar import ProgressBar
import inspect
import app
import models
from config import DATABASE
import csv

def crear_tablas():
    if os.path.exists(DATABASE['name']):
        print 'Creando el archivo ' + DATABASE['name']
        os.remove(DATABASE['name'])

    def es_un_modelo(clase):
        return inspect.isclass(clase) and issubclass(clase, models.db.Model)

    for nombre, clase in [(n, c) for n, c in inspect.getmembers(models) if es_un_modelo(c)]:
        clase.create_table(fail_silently=True)
        print 'Creando tabla para el modulo: ' + nombre

    #Crear usuario admin
    app.auth.User.create_table(fail_silently=True)
    admin = app.auth.User(username='admin', admin=True, active=True)
    admin.set_password('admin')
    admin.save()
    print "Creando al usuario administrador."

def importar_coops():
    data = csv.reader(open('Cooperativas.csv'))
    a = data.next()
    print a
    for fila in data:
        matricula, nombre = fila[0].decode('utf8'), fila[1].decode('utf8')
        print matricula, nombre
        models.Cooperativa.create(nombre=nombre, matricula=matricula)


if __name__ == '__main__':
    crear_tablas()
    importar_coops()
