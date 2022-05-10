# !/usr/bin/phtyon
# -*- coding: UTF-8 -*-

import os

commandlist = [
    'service walinuxagent status | grep Active',
    'service walinuxagent status | grep Loaded',
    'cat /etc/ssh/sshd_config | grep PermitRoot',
    ''
]
for cmd in commandlist:
    result = os.system(i)
    print(result)
