from setuptools import setup, find_packages

setup(
    name='todo',
    version='0.1',
    author='Alex Telon',
    description='A simple todo application.',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'todo = todo.cli:todo',
        ],
    },
)
