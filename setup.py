#! /usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = "funbox",
    version = "0.11.0.dev1",
    packages = find_packages(),
    author = "Nick Booker",
    author_email='nmb+pypi@nickbooker.uk',
    description = "Functional Toolbox",
    long_description="Collection of functions I find useful for FP in Python.",
    license = "MIT",
    url = "https://github.com/nmbooker/python-funbox",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='development functional',
    install_requires = [
        'functional',
    ],
)
