#!/usr/bin/env python3
import pwd
for p in pwd.getpwall():
    if p.pw_uid > 100 and not p.pw_shell.endswith('nologin'):
        print(p[0])
