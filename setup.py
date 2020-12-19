import os
import sys
"""
this assumes that the config files are located in home directory ~
needs python3.8 at least
# need to be able to setup the config
# i am not sure whether or not i will need to know the opeprating system
# this is going to be mostly bash (linux/unix)
"""
HOME = os.path.expanduser("~")

def update():
    """ copies necessary files from ~/ to . 
        Then pushes to github automatically
    """
    os.system(f"cp {HOME}/.vimrc {HOME}/configs/vimrc.txt")
    os.system(f"cp {HOME}/.tmux.conf {HOME}/configs/tmux.conf")
    os.system(f"cp {HOME}/.bashrc {HOME}/configs/bashrc.txt")
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
    """ copies necessary files from . to ~/
        If cache exists then install already happened
    """
    cacheDir = os.getcwd() + '/cache'
    cwd = os.getcwd()
    os.mkdir(cacheDir)
    listOfFiles = os.listdir(cwd)
    print(listOfFiles)

    
    if os.path.isdir(cacheDir) and not len(os.listdir(cacheDir)): 
        print("NO BASE CONFIGS FOUND DELETING CACHE")
        os.rmdir(cacheDir)

def reset():
    """ resets to original files from cache
    """
    cacheDir = os.getcwd() + '/cache'
    os.system(f"cp ./vimrc.txt {HOME}/.vimrc")
    os.system(f"cp ./tmux.conf {HOME}/.tmux.conf")
    os.system(f"cp ./bashrc.txt {HOME}/.bashrc") 

flags = {
    'update' : update,
    'install' : install,
    'reset' : reset
}
def main():
    args = sys.argv
    args.pop(0)
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
