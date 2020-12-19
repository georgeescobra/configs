import os
import sys
"""
this assumes that the config files are located in home directory ~
# need to be able to update the files
# need to be able to setup the config
# i am not sure whether or not i will need to know the opeprating system
# this is going to be mostly bash (linux/unix)
"""

def update():
    """ copies necessary files from ~/ to . """
    os.system("cp ~/.vimrc ~/configs/vimrc.txt")
    os.system("cp ~/.tmux.conf ~/configs/tmux.conf")
    os.system("cp ~/.bashrc ~/configs/bashrc.txt")
    orig = os.getcwd()
    os.chdir(orig)
    diff = os.popen("git diff").read()
    print(diff)
    #os.system("git add .")
    #os.system("git commit -m 'another update'")
    #os.system("git push")
    #os.chdir(orig)

def install():
    """ copies necessary files from . to ~/"""
    os.system("cp ./vimrc.txt ~/.vimrc")
    os.system("cp ./tmux.conf ~/.tmux.conf")
    os.system("cp ./bashrc.txt ~/.bashrc")


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
        if func := flags.get(flag, None):
            func()
        else: print('FLAG DOES NOT EXIST')

if __name__ == "__main__": main()

