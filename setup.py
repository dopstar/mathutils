from setuptools import setup

setup_args = {
    'name': 'mathutils',
    'version': '0.0.1',
    'author': 'Mkhanyisi Madlavana',
    'author_email': "mkhanyisi@gmail.com",
    'install_requires': [],
    'packages': ['mathutils', 'mathutils.games'],
}

setup(**setup_args)
