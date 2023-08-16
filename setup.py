#!/usr/bin/env python

from distutils.core import setup

import version

desc = """\
# DDT4all

DDT4All is tool to create your own ECU parameters screens and connect to a
CAN network with a cheap ELM327 interface.
"""

setup(name='DDT4all',
      version=version.__version__,
      description='ODB Tool',
      long_desc=desc,
      author=version.__author__,
      author_email=version.__email__,
      maintainer=version.__maintainer__,
      url='https://github.com/cedricp/ddt4all',
      license=version.__license__,
      packages=['ddt4all'],
      package_dir={'ddt4all': ''},
      package_data={'ddt4all': ['locale/*/*.mo']},
      data_files=[('bitmaps': ['icons/*'])],
)
