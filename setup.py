from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()  # it reads line by line all the line requirements

setup(
    name="MLOPS-PROJECT-1",
    author="Niraj",
    version="0.1.0",
    package=find_packages,
    install_requires=requirements, # used to install all requirements from the earlier declared variable requirements
)