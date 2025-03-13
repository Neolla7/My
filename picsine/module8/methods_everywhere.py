#!/usr/bin/env python3
import sys

def shrink(a):
    print(a[:8])

def enlarge(a):
    n = 8 - len(a)
    print(a + "Z" * n)

if len(sys.argv) > 1:
    for string in sys.argv[1:]:
        if len(string) < 8:
            enlarge(string)
        else:
            shrink(string)

            
