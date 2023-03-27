#!/usr/bin/env python3

from setuptools import setup

VERSION = '0.0.1'

packages = ['defillama2alpha']
requires = ['requests>=2.28.1', 'pandas>=1.4.4', 'numpy>=1.22.4']

with open('README.md', mode='r') as f:
    readme = f.read()

setup(
    name="defillama2alpha", 
    version=VERSION,
    description='Python client for DefiLlama API',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/BooniesFX/defillama2-alpha',
    author="BooniesFX",
    author_email="<booniesfx@qq.com>",
    packages=packages,
    install_requires=requires, # dependencies    
    keywords=['python 3', 'defillama', 'api'],
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)