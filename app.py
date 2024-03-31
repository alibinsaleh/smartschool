#!/usr/bin/env python3
"""Follow-up program main entry point."""
import argparse
from menu import Menu

def get_args():
    """Get command-line arguments."""
    parser = argparse.ArgumentParser(
            description='User',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('user', metavar='user', help='Input text only')
    args = parser.parse_args()
    return args


def main():
    """Make a jazz noise here"""

    args = get_args()
    user = args.user
    if user == 'alibinsaleh':
        Menu().run()
    else:
        print(f"Sorry {user}, you are not allowed to access this program, contact administrator")


if __name__ == "__main__":
    main()
