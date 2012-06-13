#! -*- coding:utf8 -*-
from peewee import *
from app import db


class Cooperativa(db.Model):
    matricula = IntegerField()
    nombre = CharField(max_lenght=255)

    def __unicode__(self):
        return u'<Cooperativa %s %s>' % (self.matricula, self.nombre)

    def to_dict(self, processed):
        data = self.get_children(processed)

        a = {
            'id':self.nombre,
            'name':self.nombre,
            'children': data
            }

        return a

    def get_federaciones(self):
        return Federacion.select().join(CoopFederacion).where(cooperativa=self)

    def get_children(self, processed):
        a = []
        for n in self.get_federaciones():
        #    if not (n.id in processed):
        #        processed.append(n.id)
            a.append(n.to_dict(processed))

        return a


class Federacion(db.Model):

    nombre = CharField(max_lenght=255)

    def __unicode__(self):
        return u'<Federación %s>' % (self.nombre)

    def get_cooperativas(self):
        return Cooperativa.select().join(CoopFederacion).where(federacion=self)

    def to_dict(self, processed):
        data = self.get_children(processed)

        a = {
            'id':self.nombre,
            'name':self.nombre,
            'children':data,
            }
        return a

    def get_children(self, processed):
        a = []
        for n in self.get_cooperativas():
            if not (n.id in processed):
                processed.append(n.id)
                a.append(n.to_dict(processed))
        return a

class CoopFederacion(db.Model):
    cooperativa = ForeignKeyField(Cooperativa, related_name='federaciones')
    federacion = ForeignKeyField(Federacion, related_name='cooperativas')

    def __unicode__(self):
        return u'<Relacion %s - %s >' % (self.cooperativa, self.federacion)


def test():
    test = '<ul>'
    for coop in Cooperativa.select().join(CoopFederacion).join(Federacion):
    #    raise ValueError
        test += "<li>%s" % coop.nombre
    test += '</ul>'
    return test

global_foo = []

def generar_diccionario_nodos():
    a = {}
    for n in Federacion.select():
        return n.to_dict([])

