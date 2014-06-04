#!/usr/bin/python3.3

"""
list the modules imported
"""

def list_em(module_name):
    the_keys = []
    for key in module_name.modules.keys():
        the_keys.append(key)

    the_keys.sort()
    maxlength = max(len(key) for key in the_keys)
    for key in the_keys:
        print(key.ljust(maxlength), '==> ', module_name.modules[key])

if __name__ == '__main__':
    import sys
    list_em(sys)
    input()
