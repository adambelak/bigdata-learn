import sys

current_cited = None
current_citing = None
cited = None
citing = None

for line in sys.stdin:
    cited, citing = line.strip().split('\t', 1)
    if current_cited == cited:
        current_citing += ',' + citing
    else:
        if current_cited:
            print '%s\t%s' % (current_cited, current_citing)
        current_cited = cited
        current_citing = citing

if current_cited == cited:
    print '%s\t%s' % (current_cited, current_citing)
