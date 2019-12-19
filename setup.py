# This repo relies on YACS heavily.
# Ross Girshick, YACS, https://github.com/rbgirshick/yacs

from setuptools import setup

setup(
    name="tacs",
    version="0.0.1",
    author="Swall0w",
    author_email="",
    description="TOML yet Another Configuration System",
    url="https://github.com/Swall0w/tacs",
    packages=["tacs"],
    long_description="A simple experiment configuration system for research in TOML",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=["toml"],
)
