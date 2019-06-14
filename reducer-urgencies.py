#!/usr/bin/env python
import sys
 
resume = {}

def putIntoResume(resume, hospital, urgencies):
    if hospital not in resume:
        resume[hospital] = urgencies
    else:
        resume[hospital] = resume[hospital] + urgencies

for line in sys.stdin:
    line = line.strip()
    hospital, urgencies = line.split('\t',1)
    putIntoResume(resume, hospital, int(urgencies))
 
for (x, y) in resume.items():
    print("%s\t%s" % (x, y))


'''
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
'''