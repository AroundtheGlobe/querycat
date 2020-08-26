import requirements

from setuptools import find_packages, setup
import os
install_requires = []

with open('requirements.txt') as fd:
    for req in requirements.parse(fd):
        if req.name:
            name = req.name.replace("-", "_")
            full_line = name + "".join(["".join(list(spec)) for spec in req.specs])
            install_requires.append(full_line)
        else:
            # a GitHub URL doesn't have a name
            # I am not sure what to do with this, actually, right now I just ignore it...


setup(name='querycat',
      version='1.0',
      author='Erik van Erp',
      author_email='development@aroundtheglobe.nl',
      url='https://github.com/AroundtheGlobe/querycat',
      packages=find_packages(),
      install_requires=install_requires,
      test_suite='tests',
      dependency_links=[

      ]
      )