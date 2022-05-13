Esta carpeta está destinada a almacenar los datos necesarios para el desarrollo del aplicativo, a continuación una breve descripción de cada una de las carpetas:

- __AUXILIAR__: contiene algunos fichero generales auxiliares necesarios como puedan ser las regiones.

- __PRINCING__: Recopilación de todos los datos de precios sobre cada una de las principales empresas de cloud (AWS, Azure y GCP). 

   Dentro de esta hay una carpeta para cada una de ellas con los datos de los servicios seleccionados y el fichero Python que recolecta la información de los precios para esa empresa. 
   
   Además de las carpetas también hay 2 ficheros:

   - _compare.json_: comparación de todos los servicios descargados entre las 3 empresas. Está etiquetado cada servicio para ser más sencillos de encontrar.
   - _config.toml_: fichero de configuración de los ficheros Python que recuperan la información de las APIs.

- __SLA__: Recopilación de los datos de SLA de cada una de las principales empresas cloud.