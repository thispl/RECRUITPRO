# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in recruitpro/__init__.py
from recruitpro import __version__ as version

setup(
	name='recruitpro',
	version=version,
	description='app recruitpro',
	author='teampro',
	author_email='sharmila.h@teampro.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
