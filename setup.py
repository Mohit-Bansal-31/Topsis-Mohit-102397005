from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Topsis technique for MCDM'
LONG_DESCRIPTION = 'A package that implements the TOPSIS technique for MCDM'

# Setting up
setup(
    name="Topsis-Mohit-102397005",
    version=VERSION,
    author="Mohit Bansal",
    author_email="mohitbansal0031@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy','sys'],
    keywords=['python', 'topsis', 'mcdm', 'decision making'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)