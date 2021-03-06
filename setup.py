#!/usr/bin/env python

from distutils.core import setup

setup(name='imup',
      description='Upload an image to an image host and return the link to the file.',
      author='Profpatsch',
      author_email='mail@profpatsch.de',
      url='https://github.com/Profpatsch/imup',
      package_dir={'imup': 'src'},
      packages=['imup', 'imup.hosts'],
      scripts=['imup'],
     )
