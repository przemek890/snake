from setuptools import setup, find_packages

setup(
    name='Snake_module',
    version='0.1',
    packages=find_packages(),
    package_data={
        'Snake_module': ['tools/*', 'snake/*', 'run.py'],
    },
    install_requires=[
        'pytest',
        'matplotlib'
    ],
)
