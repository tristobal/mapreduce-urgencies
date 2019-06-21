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
    hospital, year, urgencies = line.split('\t',2)
    key = hospital + '-' + year
    putIntoResume(resume, key, int(urgencies))
 
for (k, v) in resume.items():
    hospital, year = k.split('-', 1)
    urgencies = v
    print("%s\t%s\t%s" % (hospital, year, urgencies))
