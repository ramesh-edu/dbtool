#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0','cx_Oracle>=6.1']

setup(
    author="Ramesh Gopisetty",
    author_email='rameshg2@illinois.edu',
    classifiers=[
        'Programming Language :: Python :: 3.6'
    ],
    description="For Commandline Arugument",
    entry_points={
        'console_scripts': [
            'dbshift=dbshift.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' ,
    keywords='dbshipt',
    name='dbshipt',
    scripts=['bin/dbshipt'],
    packages=['lib','conf','sqlqueries'],
    package_dir={'lib':'lib','conf':'conf','sqlqueries':'sqlqueries'},
    include_package_data=True,
    url='github_url',
    version='1.0.0',
    zip_safe=False,
)
