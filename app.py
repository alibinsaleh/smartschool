#!/usr/bin/env python3
"""Follow-up program main entry point."""
import argparse
from menu import Menu

def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
            description='Protects program by supplying a username to get full access.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('username', metavar='username', help='username must be text only')
    args = parser.parse_args()
    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    username = args.username
    if username == 'alibinsaleh':
        Menu().run()
    else:
        print(f"Sorry {username}, you are not allowed to access this program, contact administrator")


if __name__ == "__main__":
    main()
