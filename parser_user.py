#!/usr/bin/python 
import argparse

parser = argparse.ArgumentParser(description='Process some integer.')
parser.add_argument('--foo', action='append', type=int)
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=sum,
                   help='sum the integer (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.foo)
