# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Teste-de-Reconhecimento-de-voz',
    version='0.1.0',
    description='Um simples codigo sobre reconhecidimento de voz',
    long_description=readme,
    author='Felipe Baz Mitsuishi',
    author_email='felipe.mitsuishi@unifesp.br',
    url='https://github.com/Felipe-Baz/Teste-de-Reconhecimento-de-voz',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

