# !/usr/bin/phtyon
# -*- coding: UTF-8 -*-

import os

commandlist = [
    'hostname',
    'service walinuxagent status | grep Active',
    'service walinuxagent status | grep Loaded',
    'service waagent status | grep Active',
    'service waagent status | grep Loaded',
    'service vasd status | grep Active',
    'service vasd status | grep Loaded',
    'cat /etc/ssh/sshd_config | grep PermitRoot',
    'ifconfig',
    'cat /etc/*release*',
    'cat /etc/network/interfaces',
    'cat /etcn/netplan/*',
    'cat /etc/systemd/resolved.conf',
    'cat /etc/resolvconf/resolv.conf.d/tail'
]
for cmd in commandlist:
    print("\n\n!! START\n", cmd)
    os.system(cmd)
    print("\n!! END", cmd)
