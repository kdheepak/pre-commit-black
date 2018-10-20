#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from codecs import open
from setuptools import setup, find_packages

logger = logging.getLogger(__name__)

try:
    from pypandoc import convert_text
except ImportError:
    convert_text = lambda string, *args, **kwargs: string

here = os.path.abspath(os.path.dirname(__file__))

with open("README.md", encoding="utf-8") as readme_file:
    readme = convert_text(readme_file.read(), "rst", format="md")

version = "v0.1.0"

test_requires = ["pytest"]
install_requires = ["black"]

setup(
    name="black-pre-commit",
    version=version,
    description="Black",
    long_description=readme,
    author="Dheepak Krishnamurthy",
    author_email="me@kdheepak.com",
    url="https://github.com/kdheepak/pre-commit-black",
    packages=find_packages(),
    include_package_data=True,
    license="BSD license",
    zip_safe=False,
    keywords="helics",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",  # TODO: Change development status
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    test_suite="tests",
    install_requires=install_requires,
)
