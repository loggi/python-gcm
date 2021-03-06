from setuptools import setup

setup(
    name='python-gcm',
    version='0.2',
    packages=['gcm'],
    license=open('LICENSE').read(),
    author='Nam Ngo',
    author_email='nam@kogan.com.au',
    url='http://blog.namis.me/python-gcm/',
    description='Python client for Google Cloud Messaging for Android (GCM)',
    long_description=open('README.rst').read(),
    keywords='android gcm push notification google cloud messaging',
    install_requires=['requests'],
    tests_require=['mock'],
)
