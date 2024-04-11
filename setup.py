from setuptools import setup, find_packages

setup(
    name='Snake_module',
    version='0.1',
    packages=find_packages(where='Snake_module'),
    package_dir={'': 'Snake_module'},
    install_requires=[
        'pytest',
        'matplotlib'
    ],
)
