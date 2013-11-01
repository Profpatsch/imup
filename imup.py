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
from urllib2 import URLError, HTTPError

VERSION = (0, 2, 1)
HOSTS = [s for s in dir(hosts) if not s.startswith('__')
                                  and s != 'imagehost']


def main():
    args = _parse_args()
    register_openers()

    # Logging
    if args.verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    # Try until there is no server left to try.
    #TODO: Test non-working imagehosts!
    while True:
        try:
            # If no host specified, try every host available.
            if not args.imagehost:
                host = choice(HOSTS)
                log.debug("Trying host {}".format(host))
                HOSTS.remove(host)
                if not HOSTS:
                    sys.exit("There is no more host to try.")
            elif args.imagehost not in HOSTS:
                sys.exit("This host isn’t available (yet). Try one of: {}."
                        .format(", ".join(HOSTS)))
            else:
                host = args.imagehost
            _print_link(_get_host(host), args.filename)
            sys.exit(0)
        except URLError as e:
            if hasattr(e, 'reason'):
                log.error(
                        "Couldn’t contact server. Check your network connection.")
                log.debug(str(e.reason))
                sys.exit(1)
            elif hasattr(e, 'code'):
                if HOSTS:
                    log.debug("This image host returned an error.")
                else:
                    log.error("The image host returned an error. Maybe try again?")
                    log.debug(str(e.code))
                    sys.exit(1)
        except ImagehostError as e:
            if args.imagehost: #TODO Same above.
                log.debug(e.args[0])
                sys.exit("The image host encountered a problem. -v for debug info.")
            else:
                log.debug("This image host doesn’t work. It says:\n{}"
                        .format(e.args[0]))
        except IOError as e:
            log.error(e.args[0])
            sys.exit(1)


def _get_host(host):
    """Get host object."""
    # Gets the module.
    mHost = getattr(globals()['hosts'], host)
    # Gets the class.
    clHost = getattr(mHost, host.capitalize())
    # Gets the object.
    return clHost()


def _parse_args():
    p = argparse.ArgumentParser(description=
    """Takes a filename to an image, uploads it to the specified image host
       (random if none given) and returns the link to the uploaded image.  """)
    p.add_argument("-i", "--imagehost", metavar="hostname",
            help="Specify the image host. One of: "+", ".join(HOSTS))
    p.add_argument("-v", "--verbose", action='store_true')
    p.add_argument("-V", "--version", action='version',
                    version=".".join(str(i) for i in VERSION))
    p.add_argument("filename")
    return p.parse_args()


def _print_link(host, filename):
    """Get link and print it to command line"""
    link = host.get_link(filename)
    print(link)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log.info("Interrupt received.")
