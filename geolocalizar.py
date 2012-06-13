
import json
import codecs
import sys
from googlemaps import GoogleMaps

gmaps = GoogleMaps('ABQIAAAAbwWYBdNDWhSrlUDhnHoOzhRSZLIMLGsAILtzGCo_JdRkl29wtRTgPiY-xKbabP9VEHL8y3eZuIHvPw')

#CALLE, LOCALIDAD, ERROR = range(3)

coops = json.load(codecs.open('./datos/Cooperativas.json', 'r', 'utf-8'))['rows']
fallidas = 0

salida = []

for i, coop in enumerate(coops[:100]):
    direccion = "%s %s" % (coop['Localidad'], coop['PROVINCIA'])
    try:
        lat, lng = gmaps.address_to_latlng(direccion)
    except:
        fallidas += 1
        lat,lng = -34.506132,-58.162336 #Rio de La Plata
    #print direccion,lat,lng
    print "fallaron %d / %d\r" % (fallidas, i+1),
    sys.stdout.flush()
    coop['lat'], coop['long'] = lat, lng
    salida.append(coop)

json.dump({'rows': salida}, codecs.open('./datos/Cooperativas_geo.json', 'w', 'utf-8'), indent=0, ensure_ascii=False, encoding='utf-8')
