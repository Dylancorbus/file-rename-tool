import os
import sys
import re

print sys.argv

path = sys.argv[1]

list = os.listdir(path)

print list

def navigateFileTree(workingPath, items):
    print 'checking for files in : ' + workingPath
    for item in items:
        newPath = workingPath + '/' + item
        print newPath 
        if os.path.isdir(newPath):
            newList = os.listdir(newPath)
            print 'found directory, recursivly going into: ' + newPath
            navigateFileTree(newPath, newList)
        elif os.path.isfile(newPath):
            print rename(newPath)
        else:
            print 'no item'

def rename(path):
    if os.path.isfile(path):
        src = path
        dst = re.sub(r" \(.+?\)", "", src, flags=re.I)
        os.system('chflags nouchg {}'.format(src))
        os.rename(src, dst)
        return 'CHANGED {src} TO {dst}'.format(src=src, dst=dst)
    else:
        return 'WHAT IS THIS' + path


navigateFileTree(path, list)

