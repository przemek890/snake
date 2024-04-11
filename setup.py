from setuptools import setup, find_packages

setup(
    name='Snake_module',
    version='0.1',
    packages=find_packages() + ['tools'],
    py_modules=['run'],
    install_requires=[
        'pytest',
        'matplotlib'
    ],
)
