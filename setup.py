import os
from setuptools import setup
import sys

if sys.version_info[0] < 3:
    raise Exception('Hungarian algorithm requires Python 3')

distmeta = {}
for line in open(os.path.join('hungarian_algorithm', '__init__.py')):
    try:
        field, value = (x.strip() for x in line.split('='))
    except ValueError:
        continue
    if field == '__version_info__':
        value = value.strip('[]()')
        value = '.'.join(x.strip(' \'"') for x in value.split(','))
    else:
        value = value.strip('\'"')
    distmeta[field] = value
    
long_description = "See {}".format(distmeta["__url__"])

setup(
    name="hungarian_algorithm",
    version=distmeta["__version_info__"],
    description="Implementation of the Hungarian (Munkres) algorithm in python.",
    long_description=long_description,
    author=distmeta["__author__"],
    url=distmeta["__url__"],
    license="MIT",
    packages=["hungarian_algorithm"],
    python_requires='~=3.0',
    install_requires=["numpy"],
    classifiers=[
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
    ],
    keywords = "hungarian algorithm"
)
