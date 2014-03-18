# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='issues',
    version='0.0.1',
    description='Cmd-line github issue printing',
    long_description=readme,
    author='Reid Draper',
    author_email='reiddraper@gmail.com',
    url='github.com/reiddraper/issues',
    license=license,
    package_dir={'issues': 'issues'},
    packages=find_packages('.', exclude=('tests', 'docs')),
    scripts=['bin/issues']
)

