#!/usr/bin/env python
import sys

current_hospital = None 
count_urgencies = 0
hospital = None

for line in sys.stdin:
    line = line.strip();
    hospital, urgencies = line.split('\t',1) 
    urgencies = int(urgencies)
     
    if current_hospital == hospital:
        count_urgencies += int(urgencies)
    else:
        if current_hospital:
           print("%s\t%s" % (current_hospital, count_urgencies))
        count_urgencies = urgencies
        current_hospital = hospital

if current_hospital == hospital:
	print("%s\t%s" % (current_hospital, count_urgencies))