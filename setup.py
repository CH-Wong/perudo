#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='perudo',
    url='https://github.com/CH-Wong/perudo',
    version='0.0.1',
    description="Perudo game simulator",
    long_description=readme,
    author="Chun Heung Wong",
    author_email='w.chunheung@gmail.com',
    packages=find_packages(include=['perudo', 'perudo.*']),
    install_requires=[
        "setuptools==58.0.0",
    ],
    entry_points={
        'console_scripts': [
            'perudo=perudo.Perudo:main',
        ],
    },
)