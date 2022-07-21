#!/usr/bin/env python

from distutils.core import setup

from importlib_metadata import entry_points

setup(name='Optm_ParserEngine',
      version='1.1.0',
      description='Python Regex Parser Engine',
      author='Gurmukhnishan Singh',
      author_email='info@gurmukhnishansingh.me',
      packages=['OptmPE'],
      entry_points={
            'console_scripts': ['OptmPE=OptmPE.__main__:main'],
      },
      package_data={'':[
            "Config.json"
      ]}
     )