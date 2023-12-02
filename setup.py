from setuptools import setup, find_packages

setup(
    name="Cupid-GPT",
    version="0.0.1",
    description="YeSWECan Hackathon Project",
    author="Jingchao (Perry) Zhong, Chang Lu, Taiga Kitao, Wilson Lai",
    author_email="",
    license="Apache License, Version 2.0",
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.8',
    include_package_data=True,
    install_requires = open('requirements.txt').readlines(),
)
