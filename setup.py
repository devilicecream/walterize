#!/usr/bin/env python
"""
Special thanks to Gas (gas@ovalmoney.com)
"""
from setuptools import find_packages, setup

project = "walterize"
version = "0.0.2"

setup(
    name=project,
    version=version,
    description="Pure Python implementation of the walterize algorithm for string manipulation",
    author="Walter Galante",
    author_email="walter.galante@ovalmoney.com",
    url="https://github.com/devilicecream/walterize",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    setup_requires=["nose>=1.3.6"],
    dependency_links=[],
    entry_points={},
    extras_require={"test": ["coverage>=3.7.1", "mock>=1.0.1", "PyHamcrest>=1.8.5"]},
)
