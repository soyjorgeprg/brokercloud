import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('json/config.toml')
URL = config['URL.AWS']['BASE']

r = requests.get(URL + '/offers/v1.0/aws/index.json')
dictionary= r.json()

if(r.status_code == 200 and dictionary['formatVersion'] == 'v1.0'):
    offers = dictionary['offers']
    list = config['SERVICIOS.AWS']
    for elem in list:
        service = str(config['SERVICIOS.AWS'][str(elem)])
        serviceURL = offers[str(service)]['currentVersionUrl']
        req = requests.get(URL + serviceURL)
        print("Comienza la escritura en fichero " + elem + ".json: ")
        with open('json/AWS/data/' + elem + '.json', 'w') as outfile:
            json.dump(req.json(), outfile)
        print("Siguiente servicio")
else:
    print("Problema con el indice general de los precios de AWS")