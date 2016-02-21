#!/usr/bin/env python3

import markdown2, os, sys

def generate_post(source, destination):
    with open(source) as mrkdwn:
        mdr = mrkdwn.read()
    html = markdown2.markdown(mdr)
    i = os.listdir(sys.argv[2])
    length = len(i)
    count = 0
    while length>0:
        if destination.split('/')[-1] == i[length-1]:
            with open(os.path.join(sys.argv[2], i[length-1])) as check:
                if html == check.read():
                    pass
                else:
                    with open(destination, 'w') as ohtml:
                        htmlw = ohtml.write(html)
        else:
            count += 1
        length -= 1
    if count == len(i):
        with open(destination, 'w') as ohtml:
            htmlw = ohtml.write(html)



def find_mdf(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.md'):
            htmlf = file.split('.')[0] + '.html'
            generate_post(os.path.join(path, file), os.path.join(sys.argv[2], htmlf))

find_mdf(sys.argv[1])
