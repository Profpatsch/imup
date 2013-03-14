#!/usr/bin/env python
# −*− coding: UTF−8 −*−
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

import hosts

from libposter.streaminghttp import register_openers #The reason this is
python2… can someone please port it?

from random import choice
import argparse
import sys

VERSION = (0, 1, 0)
HOSTS = [s for s in dir(hosts) if not s.startswith('__')
                                  and s != 'imagehost']

if __name__ == "__main__":

    p = argparse.ArgumentParser(usage=
    """Takes a filename to an image, uploads it to the specified image host
       (random if none given) and returns the link to the uploaded image.
       
       Try
       imup --help
       """)
    p.add_argument("-i", "--imagehost", metavar="hostname",
            help="Specify the image host. One of: "+", ".join(HOSTS))
    p.add_argument("-v", "--verbose", action='store_true')
    p.add_argument("-V", "--version", action='version',
                    version=".".join(str(i) for i in VERSION))
    p.add_argument("filename")
    args = p.parse_args()
    register_openers()

    shost = args.imagehost if args.imagehost else choice(HOSTS)
    if shost not in HOSTS:
        print "This host isn’t available (yet). Try one of: "+", ".join(HOSTS)
        sys.exit(-1)
    # Gets the module.
    mhost = getattr(globals()['hosts'], shost)
    # Gets the class.
    clhost = getattr(mhost, shost.capitalize())
    # Gets the object.
    host = clhost()

    print host.get_link(args.filename)

    #TODO: Handle errors
    #TODO: Return to stdout
