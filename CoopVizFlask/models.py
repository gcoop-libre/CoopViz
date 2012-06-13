#! -*- coding:utf8 -*-
from peewee import *
from app import db

class Cooperativa(db.Model):
    matricula = IntegerField()
    nombre = CharField(max_lenght=255)

    def __unicode__(self):
        return u'<Cooperativa %s %s>' % (self.matricula, self.nombre)


class Federacion(db.Model):

    nombre = CharField(max_lenght=255)

    def __unicode__(self):
        return u'<Federación %s>' % (self.nombre)


class CoopFederacion(db.Model):
    cooperativa = ForeignKeyField(Cooperativa)
    federacion = ForeignKeyField(Federacion)
    def __unicode__(self):
        return u'<Relacion %s - %s >' % (self.cooperativa, self.federacion)

