#!/usr/bin/env python3
import sys

def greetings(name=None):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    elif name is None: 
        print("Hello, noble stranger.")
    else: 
        print("Error! It was not a name.")
    
greetings("Ira")
greetings()
greetings(42)