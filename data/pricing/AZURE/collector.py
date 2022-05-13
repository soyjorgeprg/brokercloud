import requests
import configparser
import json

config = configparser.ConfigParser()
config.read('json/config.toml')
URL = config['URL.AZURE']['BASE']
FILTER = config['URL.AZURE']['FILTER']

list = config['SERVICIOS.AZURE']
for elem in list:
    service = str(config['SERVICIOS.AZURE'][str(elem)])
    i = 0
    fichero = elem.replace(" ", "")
    nextPage = URL + FILTER + ' eq \'' + service + '\''
    while(nextPage):
        r = requests.get(nextPage)
        print("Comienza la escritura en fichero " + fichero + '_' + str(i) + ".json: ")
        with open('json/AZURE/data/' + fichero + '_' + str(i) + '.json', 'w') as outfile:
            json.dump(r.json(), outfile)
        i+=1
        out = r.json()
        nextPage = out['NextPageLink']
    print("Siguiente servicio")