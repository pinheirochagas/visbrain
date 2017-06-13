#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
import pip
from pip.req import parse_requirements
from optparse import Option
from distutils.sysconfig import get_python_lib

__version__ = "0.2.3"
NAME = 'visbrain'
AUTHOR = "Visbrain developpers"
MAINTAINER = "Etienne Combrisson"
EMAIL = 'e.combrisson@gmail.com'
KEYWORDS = "brain MNI GPU visualization data OpenGL vispy neuroscience " + \
           "sleep data-mining"
DESCRIPTION = "Hardware-accelerated data visualization for neuroscientific data in Python"
URL = 'http://etiennecmb.github.io/visbrain/'
# Data path :
PACKAGE_DATA = {'visbrain.brain.base.template': ['*.npz'],
                'visbrain.sleep.ico': ['*.svg'],
                'visbrain.utils.topo': ['*.npz']
                }


def read(fname):
    """Read README and LICENSE."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


options = Option('--workaround')
options.skip_requirements_regex = None
REQ_FILE = './requirements.txt'
# Hack for old pip versions: Versions greater than 1.x
# have a required parameter "sessions" in parse_requierements
if pip.__version__.startswith('1.'):
    install_reqs = parse_requirements(REQ_FILE, options=options)
else:
    from pip.download import PipSession  # pylint:disable=E0611
    options.isolated_mode = False
    install_reqs = parse_requirements(REQ_FILE,  # pylint:disable=E1123
                                      options=options,
                                      session=PipSession)

REQS = [str(ir.req) for ir in install_reqs]


setup(
    name=NAME,
    version=__version__,
    packages=find_packages(),
    package_dir={'visbrain': 'visbrain'},
    package_data=PACKAGE_DATA,
    include_package_data=True,
    description=DESCRIPTION,
    long_description=read('README.md'),
    platforms='any',
    setup_requires=['numpy'],
    install_requires=REQS,
    dependency_links=[],
    author=AUTHOR,
    maintainer=MAINTAINER,
    author_email=EMAIL,
    url=URL,
    license=read('LICENSE'),
    keywords=KEYWORDS,
    classifiers=["Development Status :: 3 - Alpha",
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Education',
                 'Intended Audience :: Developers',
                 'Topic :: Scientific/Engineering :: Visualization',
                 "Programming Language :: Python :: 3.5"
                 ])
