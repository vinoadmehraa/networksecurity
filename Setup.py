'''
The setup.py file is an essential part of packaging and distributing python projects.
It is used to setuptools (or distutils in older python versions) to define the
configuration of your project, such as its metadata, dependancies, and more.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirement.
    """
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the requirement.txt file.
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore empty line and -e.
                if requirement and requirement!= '-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Requirements.txt file is not available.")
    return requirement_list

#print(get_requirements())

# setup the metadata
setup(
    name="Network Security",
    version="0.0.1",
    author="Vinoad Mehraa",
    author_email="Vinoad.Mehraa@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

