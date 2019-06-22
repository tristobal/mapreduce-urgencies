#!/usr/bin/env python
try:
    # for Python 2.x
    from StringIO import StringIO
except ImportError:
    # for Python 3.x
    from io import StringIO
import csv
import sys

TOTAL_CAUSAS_SISTEMA_RESPIRATORIO = '2'

for line in sys.stdin:
    line = line.strip();
    string_file = StringIO(line)
    reader = csv.reader(string_file, delimiter=',')
    for row in reader:
        causa = row[2]
        if causa == TOTAL_CAUSAS_SISTEMA_RESPIRATORIO:
            print("%s\t%s" % (row[1], row[4]))
