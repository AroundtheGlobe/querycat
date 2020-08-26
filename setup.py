from setuptools import find_packages, setup
import os

setup(name='querycat',
      version='1.0',
      author='Erik van Erp',
      author_email='development@aroundtheglobe.nl',
      url='https://github.com/AroundtheGlobe/querycat',
      packages=find_packages(),
      install_requires=['torch==1.4.0+cpu -f https://download.pytorch.org/whl/torch_stable.html',
                        'transformers',
                        'scikit-learn',
                        'spacy>=2.2.0,<2.3.0',
                        'pyfpgrowth'
                        ],
      test_suite='tests',
      dependency_links=[

      ]
      )