from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    required = f.read().splitlines()

setup(
    name='commonroad_cli',
    scripts = [
        'commonroad_cli/main.py'
    ],
    version='2023.1',
    description='Command line interface for CommonRoad scenarios',
    author='Robert Smith',
    packages=find_packages(),
    include_package_data=True,
)
