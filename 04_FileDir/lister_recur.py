#!/usr/bin/env python3.3

'''
    list files in the directory tree using recursion
'''

import sys, os

def lister(root):
    try:
        print('[' + root + ']')
        for file in os.listdir(root):
            path = os.path.join(root, file)
            if not os.path.isdir(path):
                print(path)
            else:
                lister(path)
    except:
        print('No such directory')
        
if __name__ == '__main__':
    lister(sys.argv[1])
