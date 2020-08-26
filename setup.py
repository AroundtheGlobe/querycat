from setuptools import find_packages, setup
import os


setup(name='querycat',
      version='1.0',
      author='Erik van Erp',
      author_email='development@aroundtheglobe.nl',
      url='https://github.com/AroundtheGlobe/querycat',
      packages=find_packages(),
      install_requires=['transformers','scikit-learn','umap-learn','spacy>=2.2.0,<2.3.0','pyfpgrowth'],
      dependency_links=[

      ]
      )