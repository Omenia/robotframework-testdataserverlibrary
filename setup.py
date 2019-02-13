import os
from setuptools import setup, find_packages

version = '0.0.13'

setup(name="robotframework-testdataserverlibrary",
      version=version,
      description="Test Data Server library for Robot Framework",
      author="SALabs",
      author_email="to.be.added@noexist89a887.org",
      url="https://github.com/Omenia/robotframework-testdataserverlibrary",
      install_requires=['requests', 'robotframework'],
      py_modules=['TDSlibrary'],
      classifiers=["Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6"],
      )
