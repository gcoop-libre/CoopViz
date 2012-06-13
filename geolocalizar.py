
import json
import codecs
import sys
from googlemaps import GoogleMaps

gmaps = GoogleMaps('ABQIAAAAbwWYBdNDWhSrlUDhnHoOzhRSZLIMLGsAILtzGCo_JdRkl29wtRTgPiY-xKbabP9VEHL8y3eZuIHvPw')

coops = json.load(codecs.open('./datos/Cooperativas.json', 'r', 'utf-8'))['rows']
calle, localidad , pais = 0,0,0

salida = []

for i, coop in enumerate(coops[:300]):
    direccion = "%s, %s %s" % (coop['Direccion'], coop['Localidad'], coop['PROVINCIA'])
    try:
        lat, lng = gmaps.address_to_latlng(direccion)
        precision = 'calle'
        calle += 1
    except:
        direccion = "%s %s" % (coop['Localidad'], coop['PROVINCIA'])
        try:
            lat, lng = gmaps.address_to_latlng(direccion)
            precision = 'localidad'
            localidad += 1
        except:
            lat,lng = -34.506132,-58.162336 #Rio de La Plata
            precision = 'pais'
            pais += 1

    #print direccion,lat,lng
    print "\r%d / %d / %d" % (calle, localidad, pais),
    sys.stdout.flush()
    coop['lat'], coop['long'] = lat, lng
    coop['precision'] = precision
    salida.append(coop)

json.dump({'rows': salida}, codecs.open('./datos/Cooperativas_geo.json', 'w', 'utf-8'), indent=0, ensure_ascii=False, encoding='utf-8')
