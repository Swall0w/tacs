# This repo relies on YACS heavily.
# Ross Girshick, YACS, https://github.com/rbgirshick/yacs

from setuptools import setup


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="tacs",
    version="0.0.1",
    author="Swall0w",
    author_email="",
    description="TOML yet Another Configuration System",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Swall0w/tacs",
    packages=["tacs"],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=["toml",],
)
