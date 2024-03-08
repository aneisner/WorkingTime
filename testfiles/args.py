import argparse


def say_hello(args):
    if args.vorname and not args.nachname:
        print(f'Hallo {args.vorname}!')

    if args.nachname and not args.vorname:
        print(f'Hallo Herr {args.nachname}')

    if args.vorname and args.nachname:
        print(f'Hallo Herr {args.vorname} {args.nachname}')

    #else:
    #    print('Hallo unbekannter Freund!')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--vorname')
    parser.add_argument('-n', '--nachname')

    args = parser.parse_args()
    say_hello(args)


if __name__ == "__main__":
    main()
