#!/usr/bin/python 
import argparse

parser = argparse.ArgumentParser(description='Process some float.')
parser.add_argument('float', metavar='N', type=float, nargs='?',
                   help='an float for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=len,
                   help='sum the float (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.float)
