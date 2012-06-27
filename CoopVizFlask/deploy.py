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

def importar_fecootra():
    fed = models.Federacion.create(nombre="Fecootra")
    data = csv.reader(open('coops-federaciones.csv'))
    for fila in data:
        matricula, nombre = fila[2].decode('utf8'), fila[1].decode('utf8')
        nombre = nombre.title()
        if matricula.isdecimal():
            coop = models.Cooperativa.create(nombre=nombre, matricula=matricula)
            print matricula, nombre, fed.id, coop.id
            rel = models.CoopFederacion.create(cooperativa=coop, federacion=fed) 

def importar_factic():
    fed = models.Federacion.create(nombre="Facttic")
    data = csv.reader(open('coops-federaciones-factic.csv'))
    for fila in data:
        matricula, nombre = fila[2].decode('utf8'), fila[1].decode('utf8')
        nombre = nombre.title()
        if matricula.isdecimal():
            coop = models.Cooperativa.create(nombre=nombre, matricula=matricula)
            print matricula, nombre, fed.id, coop.id
            rel = models.CoopFederacion.create(cooperativa=coop, federacion=fed)
    gcoop = models.Cooperativa.select().where(nombre='Gcoop').get()
    rel = models.CoopFederacion.create(cooperativa=gcoop, federacion=fed)



if __name__ == '__main__':
    crear_tablas()
#    importar_coops()
    importar_fecootra()
    importar_factic()
