from setuptools import setup, find_packages

setup(
    name='Snake_module',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'matplotlib'
    ],
    package_data={
            'snake': ['run.py'],
        }
)
