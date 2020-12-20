#!/usr/bin/env python3
import os
import sys
"""
this assumes that the config files are located in home directory ~
needs python3.8 at least
TODO: probs need to add more files at some point
"""
HOME = os.path.expanduser("~") # home directory no trailing / 
CACHEDIR = os.getcwd() + '/cache'
IGNORE = ['sublime.txt'] # ignoring certain config files

def update():
    """ copies necessary files from ~/ to config reepo 
        Then pushes to github automatically
    """
    cwd = os.getcwd()
    listOfFiles = os.listdir(cwd)
    for nameOfFile in listOfFiles:
        if nameOfFile not in IGNORE and '.txt' in nameOfFile:
            nameOfFile = nameOfFile.rstrip('.txt')
            fileAtHome = f'{HOME}/.{nameOfFile}'
            fileAtCWD = f'{cwd}/{nameOfFile}'
            if os.path.isfile(fileAtHome): 
                os.system(f"cp {fileAtHome} {fileAtCWD}.txt ")

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
        print(f"{len(nameOfFiles)-1} FILE{'S' if len(nameOfFiles)-1 > 1 else ''} CHANGED")
        if len(nameOfFiles)-1 > 0:
            print("Files Changed:")
            for name in nameOfFiles:
                if name != "Updated: ": print(f"\t{name}") 
        newMessage = ' '.join(nameOfFiles)
        newMessage += ' on ' + date
        print()
        os.system("git pull")
        os.system("git add .")
        os.system(f"git commit -m \'{newMessage}\'")
        os.system("git push")
    else:
        print("No differences since last update")

def install():
    """ copies necessary files from config to home
    """
    cwd = os.getcwd() # has no trailing /
    if not os.path.isdir(CACHEDIR): 
        os.mkdir(CACHEDIR)
    listOfFiles = os.listdir(cwd)
    countOfCache = 1
    countOfHome = 1
    for nameOfFile in listOfFiles:
        if nameOfFile not in IGNORE and '.txt' in nameOfFile:
            nameOfFile = nameOfFile.rstrip('.txt')
            fileAtHome = f'{HOME}/.{nameOfFile}'
            fileAtCWD = f'{cwd}/{nameOfFile}'
            if os.path.isfile(fileAtHome):
                diff = os.popen(f"diff {fileAtHome} {CACHEDIR}/{nameOfFile}.txt").read()
                if diff:
                    os.system(f"cp {fileAtHome} {CACHEDIR}/{nameOfFile}.txt")
                    print(f"{countOfCache}: copied last version of {nameOfFile} from HOME to {CACHEDIR}")
                    countOfCache += 1

                diff = os.popen(f"diff {fileAtHome} {cwd}/{nameOfFile}.txt").read()
                if diff: # only copies if file in git repo different from home
                    os.system(f"cp {fileAtCWD}.txt {fileAtHome}")
                    print(f"{countOfHome}: copied {nameOfFile}.txt from configs repo to {HOME}")
                    countOfHome += 1
            elif not os.path.isfile(fileAtHome): 
                os.system(f"cp {fileAtCWD}.txt {fileAtHome}")
                print(f"{countOfCache}: copied version of {nameOfFile} from CONFIGS to {CACHEDIR}")
                countOfCache += 1

    if not countOfCache-1 and not countOfHome-1: print("NO FILES WERE COPIED/CHANGED")
    if os.path.isdir(CACHEDIR) and not len(os.listdir(CACHEDIR)): 
        print("NO BASE CONFIGS FOUND DELETING CACHE")
        os.rmdir(cacheDir)

def reset():
    """ resets to last version of the file from cache
        ADD FLAH TO EXCLUIDE CERTAIN FILES
    """
    if not os.path.isdir(CACHEDIR):
        print("NO CACHE TO RESET FROM TRY GIT PULL AND --INSTALL")
    else:
        listOfFiles = os.listdir(CACHEDIR)
        print(listOfFiles)
        for fileName in listOfFiles:
            fileName = fileName.rstrip('.txt')
            fileAtHome = f'{HOME}/.{fileName}'
            if not os.system(f"cp {CACHEDIR}/{fileName}.txt {fileAtHome}"):
                print(f"Reset {fileAtHome} with {CACHEDIR}/{fileName}")

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

