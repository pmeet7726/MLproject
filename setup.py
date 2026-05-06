from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->list[str]:

    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file:
        requirements = file.readline()
        requirements = requirements.strip().split("\n")
    
        if "-e ." in requirements:
            requirements.remove("-e .") 
    return requirements

setup(
    name="MLproject",
    version="0.1.0",
    author="Meet Patel",
    author_email="pmeet7726@gmail.com",
    description="A machine learning project",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  
)