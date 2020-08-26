from setuptools import find_packages, setup
import os

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='querycat',
      version='1.0',
      author='Erik van Erp',
      author_email='development@aroundtheglobe.nl',
      url='https://github.com/AroundtheGlobe/querycat',
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      dependency_links=[

      ]
      )