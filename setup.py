#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='plottyboi',
    url='https://github.com/DelftCircuits/plottyboi',
    version='3.0.0',
    description="Data import, export and analysis software for Delft Circuits B.V.",
    long_description=readme,
    author="Chun Heung Wong",
    author_email='w.chunheung@gmail.com',
    packages=find_packages(include=['perudo', 'perudo.*']),
    install_requires=[
        "setuptools==58.0.0",
    ],
    entry_points={
        'console_scripts': [
            'p=perudo.Perudo:main',
        ],
    },
)