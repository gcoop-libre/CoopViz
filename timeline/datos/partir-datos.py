#!/usr/bin/env python
# -*- coding: utf8 -*-

#
# Script para partir el archivo json con los datos de las cooperativas
# en varios archivos con menor cantidad de entradas, en el formato
# necesario para cargar los eventos en la línea de tiempo de simile.
#

import sys

if len(sys.argv) < 2:
  print('uso: %s archivo_entrada lineas' % sys.argv[0])
  exit(1)

header ="""
{
  "dateTimeFormat": "iso8601",
  "events" : [
"""

footer = """
  ]
}
"""

archivo = sys.argv[1]
if len(sys.argv) == 4:
  archivo_nuevo = sys.argv[2]

lineas = int(sys.argv[2])
original = open(archivo, 'r')
salida = open(archivo.replace('.json', '') + '0.json', 'w')

count = 0
nro_archivo = 1
for l in original.readlines():
  if count % lineas == 0:
    salida.write(footer)
    salida.close()
    salida = open('BORRAR-%s-%d.json' % (archivo.replace('.json', ''), nro_archivo), 'w')
    salida.write(header)
    count = 0
    nro_archivo += 1

  salida.write(l)
  count += 1

original.close()
salida.close()
