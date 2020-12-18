#!/usr/bin/env python3
import os
import sys
# need to be able to update the files
# need to be able to setup the config
# i am not sure whether or not i will need to know the opeprating system
# this is going to be mostly bash (linux/unix)
def update():
    print('updating')
    return 1

def install():
    print('install')

flags = {
    'update' : update,
    'install' : install,
    'reset' : install
}
def main():
    args = sys.argv
    args.pop(0)
    print(args)
    hasFlag = False
    if args: hasFlag = True if '--' in args[0] else False
    else: install() # this will be default if only setup.py is ran
    if hasFlag:
        flag = args.pop(0)
        flag = flag.strip('--')
        if ret := flags.get(flag, None):
            ret()
        else: print('FLAG DOES NOT EXIST')

if __name__ == "__main__": main()

