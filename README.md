# Tarea Mapreduce

Sobre una planilla con listado de atenciones de urgencia del 2018 de Santiago de Chile se ejecutan un algoritmo mapreduce en python para mostrar el total de atenciones por centro establecimiento.

## Datos Originales

### Variables de la base de datos del sistema de Atenciones de Urgencia

*Ministerio de Salud- Departamento de Estadística e Información de Salud*

| Campo | Descripción |
|-------|-------------|
| IdEstablecimiento | Código de Establecimiento. |
| NEstablecimiento  | Nombre de Establecimiento |
| IdCausa | Código de Causa |
| GlosaCausa | Descripción de Causa |
| Col01 | Total de personas atendidas |
| Col02 | Menores de 1 año |
| Col03 | 1 - 4 años |
| Col04 | 5 - 14 años |
| Col05 | 15 - 64 años |
| Col06 | 65 y más años |
| fecha | Fecha |
| semana | Semana Estadística del año correspondiente | 
| GLOSATIPOESTABLECIMIENTO | Tipo de Establecimiento |
| GLOSATIPOATENCION | Tipo de Atención |
| GlosaTipoCampana | Tipo de Campaña |

### Temperatura

Mediciones de Stgo (estación Quilicura).

| Timestamp medición | Temperatura |
|--------------------|-------------|
| 01/01/2008 00:00   | 27.2        |
| 01/01/2008 03:00   | 22.2        |
| 01/01/2008 06:00   | 18.7        |
| 01/01/2008 09:00   | 15.2        |
| 01/01/2008 12:00   | 21.9        |
| 01/01/2008 15:00   | 28.8        |
| ...                | ...         |


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

## Ejecución Spark

La ejecución en Spark está detallada en el notebook [tarea2_spark.ipynb](https://github.com/tristobal/mapreduce-urgencies/blob/master/tarea2_spark.ipynb)

## Ejecucicón Hive

Se crea la tabla cuidando de respetar la ',' dentro de caracteres con comillas dobles.

```sql
create table urgencias_final(id string,
nombre string,
comuna string,
total bigint,
fecha string,
semana int,
avg double,
max double,
min double)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
   "separatorChar" = ",",
   "quoteChar"     = "\"");

LOAD DATA LOCAL INPATH '/user/jsanchez/rgencias2008_2019.csv' OVERWRITE INTO TABLE urgencias_final;
```

Luego para ejecutar la consulta:
```sql
SELECT comuna, fecha, SUM(total) as total FROM (SELECT comuna, SUBSTR(fecha, 7, 4) AS fecha, SUM(cast(TRIM(total) as BIGINT)) as total FROM csanchez.urgencias_final GROUP BY comuna, fecha) a GROUP BY comuna, fecha ORDER BY comuna, fecha
```