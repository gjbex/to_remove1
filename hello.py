#!/usr/bin/env python

import sys

def hello_message(name):
    return f'Hello nice {name}'

def display(msg):
    print(msg)
    
if __name__ == '__main__':
    msg = hello_message(sys.argv[1])
    display(msg)