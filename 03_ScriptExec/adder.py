#!/usr/bin/env python3.3

import sys
theSum = 0
while True:
    try:
        line = input()
    except EOFError:
        break
    else:
        theSum += int(line)
print(theSum)