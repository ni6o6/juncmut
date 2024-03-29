#!/usr/bin/env python

from setuptools import setup, find_packages
 
    
setup(
    name = 'juncmut',
    version = '0.5.2',
    description='Python programs for the identification of the genomic mutation from RNA-seq data',
    url = 'https://github.com/ni6o6/',
    author = 'Naoko Iida',
    author_email = 'iida.nao08@gamil.com',
    license = '',

    classifiers = [
        'Development Status :: 5 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],

    packages = find_packages(exclude = ['docker']),
    package_data={'juncmut': ['*']},
    #install_requires = [],

    entry_points = {'console_scripts': ['juncmut = juncmut:main']}

)
