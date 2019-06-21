#!/usr/bin/env python
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
import csv
import sys

for line in sys.stdin:
    line = line.strip();
    string_file = StringIO(line)
    #id, nombre, comuna, total, fecha, semana, avg, max, min
    reader = csv.reader(string_file, delimiter=',')
    for row in reader:
        comuna = row[2]
        total = row[3]
        fecha = row[4][-4:]
        print("%s\t%s\t%s" % (comuna, fecha, total))
