#!/usr/bin/env python3.3

def later():
    import sys
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')
    
if __name__ == '___main__' :later()