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
    if diff:
        from datetime import datetime
        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        changes = os.popen("git status").read()
        changes = changes.split('\n')
        nameOfFiles = ["Updated: "]
        untrackedFiles = False
        deletedFiles = False
        for line in changes:
            if "Untracked" in line: 
                untrackedFiles = True
            if untrackedFiles and len(line.split()) == 1:
                line = line.split()
                nameOfFiles.append(line[0])   
            if "modified:" in line or "deleted:" in line:
                print(line)
                line = line.split()
                nameOfFiles.append(line[1])
               
        newMessage = ' '.join(nameOfFiles)
        newMessage += ' on ' + date
        os.system("git add .")
        os.system(f"git commit -m \'{newMessage}\'")
        os.system("git push")
    else:
        print("No differences since last update")

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

