from setuptools import setup
from setuptools import find_packages

version = "0.1.8"

setup(name="bw_sphinxtheme",
      version=version,
      description="Minimalistic sphinx theme in black and white colours",
      long_description=open("README", "r").read(),
      author="Andrey Popp",
      author_email="8mayday@gmail.com",
      url="http://pypi.python.org/pypi/bw_sphinxtheme",
      license="BSD3",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=False)
