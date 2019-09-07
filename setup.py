"""Set up the JSC2F (JSON SQL Cell to File) package"""
from setuptools import setup

setup(
    name='jsc2f',
    packages=['jsc2f'],
    version='0.1',
    license='MIT',
    description='Saves a JSON fields SQLs cell to a file, or UPDATE it back',
    author='Kyle Pericak',
    author_email='kyle@pericak.com',
    url='https://github.com/kylep/jsc2f',
    download_url='https://github.com/kylep/jsc2f/archive/v0.1.tar.gz',
    keywords=['SQL', 'JSON', 'file'],
    install_requires=[
        'click',
        'mysql-connector'
    ],
    entry_points='''
        [console_scripts]
        jsc2f=jsc2f.cli:cli
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'Topic :: Database',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
    ]
)
