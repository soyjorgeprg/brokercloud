Estos son los pasos a seguir para levantar el contenedor mongo con la bbdd actualizada:

1. docker run -it -v /$PATHTOREPO/mongo:/data/db --name mymongo -d mongo

2. docker exec -it mymongo mongosh

3. ```
    test> use services
    switched to db services
    services>
    ```
 
4. Debe haber al menos 2 bases de datos, una con nombre una fecha que será la última actualizacion de datos y otras con las regiones
---

Para cargar nuevos datos se deben seguir los siguientes pasos:

1. Copiar el fichero json deseado a la carpeta mongo del repositorio.

2. Debemos asegurarnos que ese json es un array de objetos

3. Ejecutamos la siguiente instrucción: 
  ```mongoimport --db BBDD --collection TABLA --type json --file /data/db/NOMBREFICHERO --jsonArray```
 
