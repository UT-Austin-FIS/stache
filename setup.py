import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "stache",
    version = "0.0.1",
    author = "Emily Rockman/ASMP-INT",
    author_email = "asmp-erp.integrations-tech@austin.utexas.edu",
    description = ("Useful stache API utilities"),
    license = "Copyright 2016 The University of Texas",
    url = "https://bitbucket.org/utasmpint/stache",
    packages=find_packages(),
    install_requires = ('requests>=2.8.1'),
    test_suite = "tests.suite",
    long_description = read("README.md"),
    classifiers=["Development Status :: 2 - Pre-Alpha"],
)