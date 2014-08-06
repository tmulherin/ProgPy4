#!/usr/bin/env python3.3

def outaHere():
    import os
    print('Bye os world')
    os._exit(99)
    print('Never reached')
    
if __name__ == '__main__': outaHere()