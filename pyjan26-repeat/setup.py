from setuptools import setup, find_packages

setup(
    name="pyjan26-repeat",
    version="0.4.0",
    setup_requires=['setuptools>=38.6.0', 'wheel'],
    python_requires='>=3.10',
    description="A pyjan26 plugin to generate repeated pages based on a collection's data",
    author="Josnin",
    license="MIT",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/josnin/pyjan26-plugins/tree/main/pyjan26-repeat',
    }
    )
