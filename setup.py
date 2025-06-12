from setuptools import setup


setup(
    name='database',
    version='0.0.1',
    description='Database package for my web apps',
    url='git@github.com:Andrey-Patrakov/app-common-db-package.git',
    author='Andrey Patrakov',
    author_email='a.v.patrakov95@gmail.com',
    license='MIT',
    packages=['database'],
    setup_requires=[
        'sqlalchemy==2.0.38',
        'pydantic==2.0.3',
        'pydantic-settings==2.0.3']
)
