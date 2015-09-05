#!/usr/bin/env python3
import pwd
for p in pwd.getpwall():
    if p.pw_shell.endswith('/bin/bash'):
        print(p[0])

