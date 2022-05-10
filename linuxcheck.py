# !/usr/bin/phtyon
# -*- coding: UTF-8 -*-

import os

commandlist = [
    'service walinuxagent status | grep Active',
    'service walinuxagent status | grep Loaded',
    'cat /etc/ssh/sshd_config | grep PermitRoot',
    'ifconfig',
    'cat /etc/*release*',
    '',
    '',
    ''
]
for cmd in commandlist:
    print("\n\n!! START", cmd)
    os.system(cmd)
    print("!! END", cmd)
