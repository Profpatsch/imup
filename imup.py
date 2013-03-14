#!/usr/bin/env python2
# −*− coding: UTF−8 −*−
"""
Imup
Input: Filename
Output: Link to uploaded image
Options:
    -i, --imagehost:imagehost
    -v:             verbose
    -V, --version:  version
    -h, --help:
Usage:
    imup [-v] [-i|--imagehost hostname] filename
    imup -V
"""

import hosts
from hosts.imagehost import FiletypeError, ImagehostError

# The reason this is python2… can someone please port it?
from libposter.streaminghttp import register_openers

from random import choice
import argparse
import sys
import logging as log
from urllib2 import URLError

VERSION = (0, 1, 0)
HOSTS = [s for s in dir(hosts) if not s.startswith('__')
                                  and s != 'imagehost']


def main():
    # Argparse
    p = argparse.ArgumentParser(description=
    """Takes a filename to an image, uploads it to the specified image host
       (random if none given) and returns the link to the uploaded image.  """)
    p.add_argument("-i", "--imagehost", metavar="hostname",
            help="Specify the image host. One of: "+", ".join(HOSTS))
    p.add_argument("-v", "--verbose", action='store_true')
    p.add_argument("-V", "--version", action='version',
                    version=".".join(str(i) for i in VERSION))
    p.add_argument("filename")
    args = p.parse_args()
    register_openers()

    # Logging
    if args.verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    # Get host
    shost = args.imagehost if args.imagehost else choice(HOSTS)
    if shost not in HOSTS:
        sys.exit("This host isn’t available (yet). Try one of: "+", ".join(HOSTS))
    # Gets the module.
    mhost = getattr(globals()['hosts'], shost)
    # Gets the class.
    clhost = getattr(mhost, shost.capitalize())
    # Gets the object.
    host = clhost()

    # Get link
    try:
        print host.get_link(args.filename)
    except FiletypeError as e:
        log.error(e.args[0])
        sys.exit(1)
    except URLError as e:
        log.error("Couldn’t contact server. Check your network connection.")
        log.debug(str(e.reason))
        sys.exit(1)
    except ImagehostError as e:
        log.error("The image host encountered a problem. -v for debug info.")
        log.debug(e.args[0])

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt:
        log.info("Interrupt received.")
