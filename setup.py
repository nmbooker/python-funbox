#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "funbox",
    version = "0.10",
    packages = find_packages(),
    author = "Nick Booker",
    description = "Functional Toolbox",
    license = "MIT",
    url = "https://github.com/nmbooker/python-funbox",
    install_requires = [
        'functional',
    ],
)
