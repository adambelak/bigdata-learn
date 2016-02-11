import sys

for line in sys.stdin:
    line = line.strip().split()
    for entry in line:
        citation = entry.split(',', 1)
        print '%s\t%s' % (citation[0], citation[1])
