#!/usr/bin/python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages


requires = ['numpy','scikit-learn','scikit-image']

setup(name='pyrsa',
      version='0.0',
      description='Python Representational Similarity Analysis (RSA) toolbox',
      url='https://github.com/ilogue/pyrsa',
      long_description='',
      classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Science/Research",
        ],
      author='',
      author_email='',
      keywords='neuroscience ',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="pyrsa.tests",
      )
