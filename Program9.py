# Implement a program dir_tree.py that takes a directory as argument and prints all the files in that directory recursively as a tree.
# Hint: Use os.listdir and os.path.isdir functions.

from os import walk, listdir
from os.path import isfile, join, isdir

dir = input("Enter Directory : ")

def directory(dir):
    for i in listdir(dir):
        if(isdir(join(dir,i))):
            directory(join(dir,i))
        else:
            print(join(dir,i))
        
directory(dir)