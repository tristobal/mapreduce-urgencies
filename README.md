# Tarea Mapreduce

Sobre una planilla con listado de atenciones de urgencia del 2018 de Santiago de Chile se ejecutan un algoritmo mapreduce en python para mostrar el total de atenciones por centro establecimiento.

## Ejecución

```sh
cat urgencia2018.csv | python mapper-urgencies.py | sort | python reducer-urgencies.py
``` 
