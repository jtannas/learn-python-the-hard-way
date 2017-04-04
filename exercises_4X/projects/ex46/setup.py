try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

CONFIG = {
    'description': 'My Project',
    'author': 'Joel Tannas',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'jtannas@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex46'],
    'scripts': ['bin/ex46_script'],
    'name': 'ex46'
}

setup(**CONFIG)
