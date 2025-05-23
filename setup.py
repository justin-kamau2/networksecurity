'''
The setup.py file is an essential part of packaging and
 distributing Python projects. It is used by setuptools
 (or distutils in older python versions) to define the configuration
 of your project, such as its metadata, dependencies and more
 '''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirement_lst:List[str]= []
    try:
        with open ('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst
#print(get_requirements())  <- at this point run script in terminal to see whether you get a list of packages as output

setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Justin Kamau",
    author_email = "kamaujustin63@gmail.com",
    packages = find_packages(),     #Automatically finds all Python packages in the project
    install_requires = get_requirements()       #Installs dependencies from requirements.txt
)
        