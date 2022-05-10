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
    print("####" cmd "START ####")
    os.system(cmd)
    print("####" cmd "END ####")
