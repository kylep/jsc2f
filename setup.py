"""Set up the JSC2F (JSON SQL Cell to File) package"""
from setuptools import setup

setup(
    name='jsc2f',
    version='1.00',
    author='Kyle Pericak',
    url='kyle.pericak.com/jsc2f',
    author_email='kyle@pericak.com',
    packages=['jsc2f'],
    install_requires=[
        'click',
        'mysql-connector'
    ],
    entry_points='''
        [console_scripts]
        jsc2f=jsc2f.cli:cli
    '''
)
