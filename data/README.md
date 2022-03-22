He descargado desde [esta web](https://www.paradigmadigital.com/dev/comparativa-servicios-cloud-aws-azure-gcp/) el html con las tablas para parsear todos los servicios de los principales proveedores. Pasos:
1. Limpiar el html, con un procesador de textos, de aquellas etiquetas que no servian resultando "tablas" de este estilo:
```
IaaS
<td><a href="https://aws.amazon.com/ec2/" target="_blank">Elastic Compute Cloud (EC2)
<td><a href="https://azure.microsoft.com/services/virtual-machines/" target="_blank">Azure Virtual Machines
<td><a href="https://cloud.google.com/compute/" target="_blank">Compute Engine
```

2. Luego mediante el script [parser.py](https://github.com/soyjorgeprg/brokercloud/blob/main/data/parser.py) obtuvimos un json con todos los datos recopilados.

3. TODO: Comprobar que todas las entradas tengan la misma estructura
