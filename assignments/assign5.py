#!/usr/bin/env python3
fobj = open('/proc/meminfo')
a = 2
while a >= 0:
    b = fobj.readline()
    c = b.split(':')
    e = c[1].split()
    print('%s : %f MB' % (c[0], int(e[0])/1024))
    a = a - 1
