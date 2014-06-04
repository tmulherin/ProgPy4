#!c:\Python\Python.exe

"""
split and interactively page a string or file of text
"""

def more(text, numlines=15):
    lines = text.splitlines()                   #-> like split('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and input('More?') not in ('Y', 'y'): break

    fred = input('Press any key to continue')

if __name__ == '__main__':
    import sys                                  #-> when run not when imported
    more(open(sys.argv[1]).read(), 10)          #-> page contents of file on cmdline 

    #helper = sys.__doc__
    #more(helper, 10)

# next is Introducing the sys Module