#!/usr/bin/python3.6

import argparse

def wt_options(args):
    #workinghours list
    if args.list and args.all:
        print("list + all")
    if args.list and args.day:
        print("list + day")


def main():
    # create the top-level parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', action='store_true', help='foo help')
    parser.add_argument('--bar', help='foo help')
    subparsers = parser.add_subparsers(help='sub-command help')

    # create the parser for the "list" command
    parser_a = subparsers.add_parser('list', help='a help')
    parser_a.add_argument('bar', type=int, help='bar help')

    # create the parser for the "add" command
    parser_b = subparsers.add_parser('add', help='b help')
    parser_b.add_argument('--baz', choices='XYZ', help='baz help')

    # create the parser for the "edit" command
    parser_c = subparsers.add_parser('edit', help='help me')
    # parse some argument lists

    # create the parser for the "del" command
    parser_b = subparsers.add_parser('del', help='b help')
    parser_b.add_argument('--baz', choices='XYZ', help='baz help')
    args = parser.parse_args()

    print(args.foo)
    print(args.bar)
    #wt_options(args)

if __name__ == "__main__":
    main()
