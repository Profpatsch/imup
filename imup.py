"""
Imup
Input: Filename
Output: Link to uploaded image
Options:
    -i, --imagehost:     imagehost
    -v:             verbose
    -V, --version:  version
Usage:
    imup [-v] [-i|--imagehost hostname] filename
    imup -V
"""

# Functions:
# get_link(filename): Link
# get_modules(): List of module names
#
# __main__

import argparse
from hosts import *

VERSION = (0, 1, 0)
HOSTS = ['immio']


if __name__ == "__main__":

    p = argparse.ArgumentParser(usage=
    """Takes a filename to an image, uploads it to the specified image host
       (random if none given) and returns the link to the uploaded image.""")
    p.add_argument("-i", "--imagehost", metavar="hostname",
            help="Specify the image host. One of: "+ ", ".join(HOSTS))
    p.add_argument("-v", "--verbose", action='store_true')
    p.add_argument("-V", "--version", action='version',
                    version=".".join(str(i) for i in VERSION))
    p.add_argument("filename")
    args = p.parse_args()




