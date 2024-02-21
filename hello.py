#!/usr/bin/env python

import argparse

def hello_message(name):
    return f'Hello nice {name}'

def display(msg):
    print(msg)
    
if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('name', type=str, default='world',
                            help='name to greet')
    args = arg_parser.parse_args()
    msg = hello_message(args.name)
    display(msg)
