from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in equipment_management/__init__.py
from equipment_management import __version__ as version

setup(
	name="equipment_management",
	version=version,
	description="Equipment Management",
	author="Deepak Kumar",
	author_email="deepak@korecent.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
