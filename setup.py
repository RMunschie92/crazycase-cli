from setuptools import setup
setup(
    name = 'crazycase',
    version = '0.1.0',
    packages = ['crazycase'],
    entry_points = {
        'console_scripts': [
            'crazycase = crazycase.__main__:main'
        ]
    })