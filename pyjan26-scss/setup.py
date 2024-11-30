from setuptools import setup, find_packages

setup(
    name="pyjan26-scss",
    version="0.2.0",
    setup_requires=['setuptools>=38.6.0', 'wheel'],
    python_requires='>=3.10',
    description="A plugin for compiling SCSS files into CSS during the build process in Pyjan26",
    install_requires=[
        'libsass>=0.23.0',
    ],
    author="Josnin",
    license="MIT",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/josnin/pyjan26-plugins/tree/main/pyjan26-scss',
    }
    )
