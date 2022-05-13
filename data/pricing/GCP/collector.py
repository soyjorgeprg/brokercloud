import requests
import configparser
import json
import os
from dotenv import load_dotenv

def search(services, nombre):
    for service in services:
        if service['displayName'] == nombre:
            return service['serviceId']
    return 0

load_dotenv()
config = configparser.ConfigParser()
config.read('json/config.toml')
URL = config['URL.GCP']['BASE']
KEY = config['URL.GCP']['KEY']
SKU = config['URL.GCP']['SKU']
API_KEY = os.getenv('API_KEY_GCP')

r = requests.get(URL + "?" + KEY + API_KEY)
dictionary= r.json()

if(r.status_code == 200):
    offers = dictionary['services']
    list = config['SERVICIOS.GCP']
    for elem in list:
        service = str(config['SERVICIOS.GCP'][str(elem)])
        serviceID = search(offers, service)     
        req = requests.get(URL + "/" + serviceID + "/" + SKU + "?" + KEY + API_KEY)
        index = req.json()
        fichero = elem.replace(" ", "").replace("/", "")
        print("Comienza la escritura en fichero " + fichero + "_0.json: ")
        with open('json/GCP/data/' + fichero + '_0.json', 'w') as outfile:
            json.dump(index, outfile)
        i = 1
        nextPage = index['nextPageToken']
        while(nextPage):
            req = requests.get(URL + "/" + serviceID + "/" + SKU + "?" + KEY + API_KEY + "&pageToken=" + nextPage)
            print("Comienza la escritura en fichero " + fichero + '_' + str(i) + ".json: ")
            with open('json/GCP/data/' + fichero + '_' + str(i) + '.json', 'w') as outfile:
                json.dump(req.json(), outfile)
            i+=1
            out = req.json()
            nextPage = out['nextPageToken']
        print("Siguiente servicio")
else:
    print("Problema con el indice general de los precios de AWS")