#!/usr/bin/env python
from distutils.core import setup
setup(
    name='acrobaticjson',
    version='1.0',
    description='Python Acrobatic JSON library',
    packages=['acrobaticjson'],
    provides=['acrobaticjson'],
    requries=[
        'simplejson',
    ]
)
