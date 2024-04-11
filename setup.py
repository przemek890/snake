from setuptools import setup

setup(
    name='Snake_module',
    version='0.1',
    packages=['Snake_module', 'Snake_module.snake', 'Snake_module.tools'],
    install_requires=[
        'pytest',
        'matplotlib'
    ],
    package_data={
        'Snake_module': ['run.py'],
    }
)
