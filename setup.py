from setuptools import setup, find_packages

setup(
    name='Example',
    version='1.0',
    description='Python-UI-DB-Example',
    author='Samuel Krieg',
    author_email='sikcd90@gmail.com',
    install_requires=['bar', 'greek'], #external packages as dependencies
    url='https://github.com/develmusa/Python-UI-DB-Example.git',
    license=license,
    packages=find_packages(exclude=('tests'))
)