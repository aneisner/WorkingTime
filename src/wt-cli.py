#!/usr/bin/python3.6

import argparse, pprint

def wt_options(args):
    if args.subcmd == "list":
        print("list")

    #workinghours list
    #if args.list and args.all:
    #    print("list + all")
    #if args.list and args.day:
    #    print("list + day")


def main():
    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help', dest='subcmd')

    # create the parser for the "list" command
    parser_a = subparsers.add_parser('list', help='list help')
    parser_a.add_argument('-a', '--all', action='store_true', help='all help')
    parser_a.add_argument('-d', '--day', help='day help')

    # create the parser for the "add" command
    parser_b = subparsers.add_parser('add', help='add help')
    parser_b.add_argument('-d', '--day', help='day help')
    parser_b.add_argument('-s', '--start-time', help='start-time help')
    parser_b.add_argument('-e', '--end-time', help='end-time help')
    parser_b.add_argument('-b', '--break-time', help='breaktime help')
    parser_b.add_argument('-c', '--comment', help='comment help')

    # create the parser for the "edit" command
    parser_c = subparsers.add_parser('edit', help='list help')
    parser_c.add_argument('-d', '--day', help='day help')
    parser_c.add_argument('-s', '--start-time', help='start-time help')
    parser_c.add_argument('-e', '--end-time', help='end-time help')
    parser_c.add_argument('-b', '--break-time', help='breaktime help')
    parser_c.add_argument('-c', '--comment', help='comment help')

    # create the parser for the "del" command
    parser_d = subparsers.add_parser('del', help='del help')
    parser_d.add_argument('-d', '--day', help='day help')
    parser_d.add_argument('-r', '--reset-repo', help='reset-repo help')
    parser_d.add_argument('--baz', choices='XYZ', help='baz help')

    print(type(parser))
    print(type(subparsers))
    print(type(parser_a))
    print(type(parser_b))
    print(type(parser_c))
    print(type(parser_d))

    args = parser.parse_args()
    pprint.pprint(args)

#print(args.foo)
    #print(args.bar)
    wt_options(args)

if __name__ == "__main__":
    main()
