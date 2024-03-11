#!/usr/bin/python3.6

import argparse

def wt_options(args):
	#workinghours list
	if args.list and args.all:
		print("list + all")
	if args.list and args.day:
		print("list + day")

def main():
    parser = argparse.ArgumentParser()
    #Commands
    parser.add_argument('list')
    parser.add_argument('add')
    parser.add_argument('edit')
    parser.add_argument('del')

    #Options
    parser.add_argument('-a', '--all')
    parser.add_argument('-d', '--day')
    parser.add_argument('-s', '--start-time')
    parser.add_argument('-e', '--end-time')
    parser.add_argument('-b', '--break')
    parser.add_argument('-c', '--comment')
    parser.add_argument('-r', '--reset-repo')

    args = parser.parse_args()
    wt_options(args)

if __name__ == "__main__":
    main()