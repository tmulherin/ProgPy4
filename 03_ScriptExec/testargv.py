#!/usr/bin/env python3.3

def getopts(argv):
    opts = []
    while len(argv) > 0:
        if argv[0][0] == '-':
            opts.append(argv[0])
 
        if len(argv) > 1:
            argv = argv[1:]
        else: argv = []
      
    return opts

    
if __name__ == '__main__':
    from sys import argv
    print(argv)
    myArgs = getopts(argv)
    if '-i' in myArgs:
        print(myArgs['-i'])
    print(myArgs)

    