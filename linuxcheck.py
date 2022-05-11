# !/usr/bin/phtyon
# -*- coding: UTF-8 -*-

import os
import time

# command list
commandlist = [
    'hostname',
    'python --version',
    'python3 --version',
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
    'cat /etc/netplan/*',
    'cat /etc/systemd/resolved.conf',
    'cat /etc/resolvconf/resolv.conf.d/tail'
]


def CommandRun():
    print("1) running everything at once")
    print("2) running step by step (Enter next step)")
    print("3) running every 3 second")
    number = int(input("Select Number) "))
    if number == 1:
        for cmd in commandlist:
            print()
            print("!! START !! ", cmd)
            os.system(cmd)
            print()
            print("### END ### ", cmd)
            print()
            print()
    elif number == 2:
        for cmd in commandlist:
            print()
            print("!! START !! ", cmd)
            input("")
            os.system(cmd)
            print()
            print("### END ### ", cmd)
            print()
            print()
    elif number == 3:
        for cmd in commandlist:
            time.sleep(3)
            print()
            print("!! START !! ", cmd)
            os.system(cmd)
            print()
            print("### END ### ", cmd)
            print()
            print()
    else:
        exit()


CommandRun()
