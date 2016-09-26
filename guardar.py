import urllib
import json
import pprint
import sqlite3
url = 'http://datos.gob.cl/api/action/datastore_search?resource_id=cbd329c6-9fe6-4dc1-91e3-a99689fd0254&limit=1886'
fileobj = urllib.urlopen(url)
urllib.urlretrieve(url, 'json.json')
with open('json.json') as data_file:
 data = json.load(data_file)
connection = sqlite3.connect('bip.db')
consulta= connection.cursor()
consulta.execute("CREATE TABLE IF NOT EXISTS LOCALES(ID INT(5) PRIMARY KEY,CODIGO INT(30),ENTIDAD VARCHAR(50),NOMBFANTASIA VARCHAR(50),DIRECCION VARCHAR(50),COMUNA VARCHAR(30),HORARIO VARCHAR(50),NORTE NUMERIC,LONGITUD NUMERIC,LATITUD NUMERIC)")

for x in range(0,1886):
 print x
 id =x
 entidad = data["result"]["records"][x]["ENTIDAD"]
 direccion = data["result"]["records"][x]["DIRECCION"]
 horario = data["result"]["records"][x]["HORARIO REFERENCIAL"]
 norte = data["result"]["records"][x]["NORTE"]
 longitud = data["result"]["records"][x]["LONGITUD"]
 latitud = data["result"]["records"][x]["LATITUD"]
 este = data["result"]["records"][x]["ESTE"]
 codigo = data["result"]["records"][x]["CODIGO"]
 comuna = data["result"]["records"][x]["COMUNA"]
 NonFantasia = data["result"]["records"][x]["NOMBRE FANTASIA"]
 locales=(id,codigo,entidad,NonFantasia,direccion,comuna,horario,norte,longitud,latitud)
 consulta.execute("INSERT INTO LOCALES(ID,CODIGO,ENTIDAD,NOMBFANTASIA,DIRECCION,COMUNA,HORARIO,NORTE,LONGITUD,LATITUD) VALUES(?,?,?,?,?,?,?,?,?,?)", locales)
 connection.commit()
print "Guardado Con Exito"
connection.close()