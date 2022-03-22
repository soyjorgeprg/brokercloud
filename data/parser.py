import json
import re

filename = 'data.txt'

out = {}
fields = ["AWS", "AZURE", "GCP"]

with open(filename) as fh:
  for i in range (101):
    awsService = {}
    azureService = {}
    gcpService = {}

    servicio = fh.readline()
    awsLine = fh.readline().strip().split(">")
    azureLine = fh.readline().strip().split(">")
    gcpLine = fh.readline().strip().split(">")
    emptyLine = fh.readline()

    if awsLine:
      awsServices = []
      for i in range(int((len(awsLine)-1)/2)):
        awsService["name"] = awsLine[-1+(-2*i)]
        auxAWS = re.findall('(https?://\S+)', awsLine[-2+(-2*i)])
        if auxAWS: awsService["url"] = auxAWS[0][:len(auxAWS[0])- 1]
        awsServices.append(awsService.copy())

    if azureLine:
      azureServices = []
      for i in range(int((len(azureLine) - 1) / 2)):
        azureService["name"] = azureLine[-1+(-2*i)]
        auxAZURE = re.findall('(https?://\S+)', azureLine[-2+(-2*i)])
        if auxAZURE: azureService["url"] = auxAZURE[0][:len(auxAZURE[0])- 1]
        azureServices.append(azureService.copy())

    if gcpLine:
      gcpServices = []
      for i in range(int((len(gcpLine) - 1) / 2)):
        gcpService["name"] = gcpLine[-1+(-2*i)]
        auxGCP = re.findall('(https?://\S+)', gcpLine[-2+(-2*i)])
        if auxGCP: gcpService["url"] = auxGCP[0][:len(auxGCP[0])- 1]
        gcpServices.append(gcpService.copy())

    servicios = {"AWS": awsServices, "AZURE": azureServices, "GCP": gcpServices}

    out[servicio] = servicios

out_file = open("data.json", "w")
json.dump(out, out_file, indent = 2, sort_keys = False)
out_file.close()

