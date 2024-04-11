from setuptools import setup, find_packages

setup(
    name='Snake_module',
    version='0.1',
    author='Przemysław Janiszewski',
    author_email='przemek.899@wp.pl',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'matplotlib'
    ],
)
