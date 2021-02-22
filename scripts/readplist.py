#! /usr/bin/env python3

"""
This script demonstrates how to read Apple property list files.
"""

import os
import argparse
import plistlib
import json

# Create parser
parser = argparse.ArgumentParser(
    description="Verify file size of ISO image and extract technical information")


def parseCommandLine():
    """Parse command line"""
    # Add arguments
    parser.add_argument('plist',
                        action="store",
                        type=str,
                        help="input property list")
    # Parse arguments
    args = parser.parse_args()

    return args


def main():
    """Main function"""

    # Get input from command line
    args = parseCommandLine()

    # Input file
    plistIn = os.path.abspath(args.plist)

    # Read property list to Python dictionary
    with open(plistIn, 'rb') as f:
        pl = plistlib.load(f)

    # Convert dictionary to JSON
    pl = json.dumps(pl)
    print(pl)


if __name__ == "__main__":
    main()
