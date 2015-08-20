# -*- coding: utf-8 -*-
"""
==================================
Redirect Streams Setuptools Module
==================================

:website: https://github.com/jambonrose/redirect_streams
:copyright: Copyright 2015 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""
from __future__ import unicode_literals

from setuptools import setup, find_packages
from codecs import open
from os.path import abspath, dirname, join

PROJECT_DIR = abspath(dirname(__file__))

with open(join(PROJECT_DIR, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

version = {}
init_file = join(PROJECT_DIR, 'redirect_streams', '__init__.py')
with open(init_file, encoding='utf-8') as f:
    exec(f.read(), version)

setup(
    name='redirect-streams',
    version=version['__version__'],

    keywords=['stream', 'stdout', 'stderr', 'with', 'context managers'],
    description='Easy stream redirection in Python.',
    long_description=long_description,

    url='https://github.com/jambonrose/redirect_streams',

    author='Andrew Pinkham',
    author_email='hello at andrewsforge dot com',

    license='Simplified BSD License',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    packages=find_packages(exclude=['docs', 'tests', 'requirements']),
)
