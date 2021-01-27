#!/usr/bin/env python

from setuptools import find_packages, setup

from src import validator

setup(
    name=validator.__title__,
    author=validator.__author__,
    author_email=validator.__email__,
    url="https://github.com/manchenkoff/swagger-routes-validator",
    project_urls={
        "Source": "https://github.com/manchenkoff/swagger-routes-validator",
    },
    version=validator.__version__,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    license="MIT",
    description=validator.__description__,
    long_description_content_type="text/markdown",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'openapi3-parser',
        'pyyaml',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'swagger-routes-validator=validator.__main__:run',
        ]
    },
)
