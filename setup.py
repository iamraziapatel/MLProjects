from setuptools import setup,find_packages
from typing import List


def get_requirments(file_path:str) -> List[str]:
    
    with open(file_path,"r") as file :
      req_arr  = [ line.strip() for line in file.readlines() if line.strip() != "-e ."]
    
    return req_arr
      

        
print(get_requirments("requirments.txt"))


setup(name="MLProjects",
      version="1.0",
      description="Base Credit to Krish but modifications by Razia where ever needed",
      author="razia",
      packages=find_packages(),
      install_requires=get_requirments("requirments.txt")
      )
