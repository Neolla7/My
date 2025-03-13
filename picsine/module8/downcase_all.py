#!/usr/bin/env python3
import sys

def downcase_it(a):
    return a.lower()

if len(sys.argv) > 1:
    for string in sys.argv[1:]:
        print(downcase_it(string))
else:
    print("none")