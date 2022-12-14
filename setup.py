import os
from distutils.core import setup
from BlueMoon import VERSION
from setuptools import find_packages
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='Blue-Moon',
    version=VERSION,
    packages=find_packages(),
    long_description_content_type="text/markdown",
    long_description=long_description,
    entry_points={
        'console_scripts': [
            'bluemoon = BlueMoon.app:start_server'
        ]
    },
    url='https://github.com/Subhranil-Maity/Blue-Moon-Client',
    license='',
    author='Subhranil Maity',
    author_email='thecodersubhranil@gmail.com',
    description='',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ]

)
