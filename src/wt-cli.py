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
    parser_a = subparsers.add_parser('list', help='list help')
    parser_a.add_argument('--all', action='store_true', help='all help')
    parser_a.add_argument('--day', help='day help')

    # create the parser for the "add" command
    parser_b = subparsers.add_parser('add', help='add help')
    parser_b.add_argument('--day', help='day help')
    parser_b.add_argument('--start-time', help='start-time help')
    parser_b.add_argument('--end-time', help='end-time help')
    parser_b.add_argument('--break-time', help='breaktime help')
    parser_b.add_argument('--comment', help='comment help')

    # create the parser for the "edit" command
    parser_c = subparsers.add_parser('edit', help='list help')
    parser_c.add_argument('--day', help='day help')
    parser_c.add_argument('--start-time', action='store_true', help='start-time help')
    parser_c.add_argument('--end-time', action='store_true', help='end-time help')
    parser_c.add_argument('--break-time', action='store_true', help='breaktime help')
    parser_c.add_argument('--comment', action='store_true', help='comment help')

    # create the parser for the "del" command
    parser_d = subparsers.add_parser('del', help='del help')
    parser_d.add_argument('--day', help='day help')
    parser_d.add_argument('--reset-repo', help='reset-repo help')
    parser_d.add_argument('--baz', choices='XYZ', help='baz help')

    args = parser.parse_args()

    print(args.foo)
    print(args.bar)
    #wt_options(args)

if __name__ == "__main__":
    main()
