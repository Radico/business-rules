#! /usr/bin/env python

from __future__ import absolute_import
import setuptools
from setuptools import find_packages

from business_rules import __version__ as version

with open('HISTORY.rst') as f:
    history = f.read()

description = 'Python DSL for setting up business intelligence rules that can be configured without code'

install_requires = [
    'pytz>=2016.10',
    "typing ; python_version<'3.5'",
    'six',
]

setuptools.setup(
    name='business-rules-simon',
    version=version,
    description='{0}\n\n{1}'.format(description, history),
    author='Venmo',
    author_email='wyn@simondata.com',
    url='https://github.com/Radico/business-rules',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    install_requires=install_requires
)
