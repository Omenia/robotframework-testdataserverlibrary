import os
from setuptools import setup, find_packages

requirements = []
with open("requirements.txt", "r") as f:
    requirements = list(filter(lambda s: s!="", f.read().split("\n")))

version = '0.0.4'

setup(name="robotframework-testdataserverlibrary",
      version=version,
      description="Test Data Server library for Robot Framework",
      author="SALabs",
      author_email="to.be.added@noexist89a887.org",
      url="https://github.com/Omenia/robotframework-testdataserverlibrary",
      install_requires=requirements,
      py_modules=['TDSlibrary'],
      classifiers=["Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6"],
      )
