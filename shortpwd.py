#!/usr/bin/env python

import sys
sys.path.insert(0,'/usr/lib/python2.7')

import os
from commands import getoutput
from socket import gethostname

def shorten(pwd):
    homedir = os.path.expanduser('~')
    pwd = pwd.replace(homedir, '~', 1)

    first = pwd.find('/',1)
    second = pwd.find('/',first+1)
    last = pwd.rfind('/')

    if first>-1 and second>-1:
        pwd = pwd[:first+1]+'...'+pwd[last:]
    return pwd

if __name__ == '__main__':
    hostname = gethostname()
    username = os.environ['USER']
    pwd = os.getcwd()
    print '[%s@%s:%s] ' % (username, hostname, shorten(pwd))
