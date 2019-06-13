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