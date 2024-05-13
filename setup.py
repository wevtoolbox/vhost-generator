"""Pip configuration."""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="vhost-generator",
    version="1.0.10",
    description="Configurable vHost generator for Apache 2.2, Apache 2.4 and Nginx.",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="wevtoolbox",
    author_email="wevtoolbox@gmail.com",
    url="https://github.com/wevtoolbox/vhost-generator",
    install_requires=["pyyaml", "future"],
    scripts=[
        "bin/vhost-generator"
    ],
       project_urls={
        'Source Code': 'https://github.com/wevtoolbox/vhost-generator',
        'Documentation': 'https://wevtoolbox.readthedocs.io/en/latest/',
        'Bug Tracker': 'https://github.com/wevtoolbox/vhost-generator/issues',
    },
 classifiers=[
        # https://pypi.org/classifiers/
        #
        # How mature is this project
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        "Intended Audience :: System Administrators",
        # Project topics
        'Topic :: Software Development :: Build Tools',
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        # License
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        # How does it run
        "Environment :: Console",
        # Where does it rnu
        "Operating System :: OS Independent",
    ],
 )
