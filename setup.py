#!/usr/bin/env python
# coding=utf-8

from os.path import abspath, dirname, join
import setuptools
from setuptools import find_packages, setup

setup_dir = abspath(dirname(__file__))
with open(join(setup_dir, 'requirements.txt')) as fp:
    install_requires = fp.readlines()

setup(
    name = 'iotawallet',
    description = 'Python implementation of an Iota Wallet',
    url = 'https://github.com/scottbelden/iotawallet',
    version = '0.0.6',
    packages = find_packages('.', exclude=('test',)),
    include_package_data  = True,
    entry_points = {
        'console_scripts': [
            'iotawallet=iotawallet.gui.wxapp:main',
        ],
    },
    install_requires = install_requires,
    license = 'MIT',
    classifiers = [
      'Intended Audience :: End Users/Desktop',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],
    author        = 'Scott Belden',
    author_email  = 'scottabelden@gmail.com',
)
