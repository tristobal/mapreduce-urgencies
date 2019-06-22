# Tarea Mapreduce

Sobre una planilla con listado de atenciones de urgencia del 2018 de Santiago de Chile se ejecutan un algoritmo mapreduce en python para mostrar el total de atenciones por centro establecimiento.

## Ejecución

```sh
cat urgencia2018.csv | python mapper-urgencies-v2.py | sort | python reducer-urgencies-v2.py | sort
``` 
