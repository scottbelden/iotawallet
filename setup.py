#!/usr/bin/env python
# coding=utf-8

import setuptools
from setuptools import find_packages, setup

setup(
    name = 'iotawallet',
    description = 'Python implementation of an Iota Wallet',
    url = 'https://github.com/scottbelden/iotawallet',
    version = '0.0.1',
    packages = find_packages('.', exclude=('test',)),
    include_package_data  = True,
    entry_points = {
        'console_scripts': [
            'iota-cli=iota.bin.repl:main',
        ],
    },
    install_requires = [
        'pyota',
    ],
    license = 'MIT',
    classifiers = [
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    author        = 'Scott Belden',
    author_email  = 'scottabelden@gmail.com',
)
