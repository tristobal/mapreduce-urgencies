# Tarea Mapreduce

Sobre una planilla con listado de atenciones de urgencia del 2018 de Santiago de Chile se ejecutan un algoritmo mapreduce en python para mostrar el total de atenciones por centro establecimiento.

## Ejecución en local

```sh
cat urgencias2008_2019.csv | python mapper-urgencies-v2.py | sort | python reducer-urgencies-v2.py | sort >  output-python.txt
``` 

## Ejecución en hadoop

Se copia la planilla al HDFS del cluster

```sh
hadoop fs -put urgencias2008_2019.csv
```

Luego se ejecuta map reduce en el cluster vía Hadoop:

```sh
hadoop jar /opt/cloudera/parcels/CDH-5.15.1-1.cdh5.15.1.p0.4/jars/hadoop-streaming-2.6.0-cdh5.15.1.jar -file mapper-urgencies-v2.py -mapper mapper-urgencies-v2.py -file reducer-urgencies-v2.py -reducer reducer-urgencies-v2.py -input urgencias2008_2019.csv -output output-tarea-urgencias-final
```

Para asegurar que la ejecución dio el mismo resultado que ejecutándolo directamente con python, se guardan las salidas en un archivo

```sh
hadoop fs -cat output-tarea-urgencias-final/*  | sort > output-hadoop.txt
```

