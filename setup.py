from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.31'
DESCRIPTION = 'Topsis technique for MCDM'
from pathlib import Path
this_directory = Path(__file__).parent
LONG_DESCRIPTION = (this_directory / "README.md").read_text()

# Setting up
setup(
    name="Topsis_Mohit_102397005",
    version=VERSION,
    author="Mohit Bansal",
    author_email="mohitbansal0031@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
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