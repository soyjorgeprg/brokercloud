He descargado desde [esta web](https://www.paradigmadigital.com/dev/comparativa-servicios-cloud-aws-azure-gcp/) el html con las tablas para parsear todos los servicios de los principales proveedores. Pasos:
1. Limpiar el html, con un procesador de textos, de aquellas etiquetas que no servian resultando "tablas" de este estilo:
```
IaaS
<td><a href="https://aws.amazon.com/ec2/" target="_blank">Elastic Compute Cloud (EC2)
<td><a href="https://azure.microsoft.com/services/virtual-machines/" target="_blank">Azure Virtual Machines
<td><a href="https://cloud.google.com/compute/" target="_blank">Compute Engine
```

2. Luego mediante el script [parser.py](https://github.com/soyjorgeprg/brokercloud/blob/main/data/parser.py) obtuvimos un json con todos los datos recopilados.

3. Añadir precios y etiquetas de AWS

   3.1. Problema con API Rest en Sidney y con San Paulo (falta un precio oficial en las llamadas a API Restful)

   3.2. AppFlow tanto en AWS como externo, pero conectado con AWS PrivateLink es el mismo precio

   3.3. Analizar como se debe añadir servicios como Aurora o Bracket

   3.4. Analizar la necesidad de añadir Chime