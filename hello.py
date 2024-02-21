#!/usr/bin/env python

import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', type=str, default='world',
                        help='name to greet')
args = arg_parser.parse_args()
print(f'hello nice {args.name}!')
