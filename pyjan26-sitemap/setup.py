from setuptools import setup, find_packages

setup(
    name="pyjan26-sitemap",
    version="0.5.0",
    setup_requires=['setuptools>=38.6.0', 'wheel'],
    python_requires='>=3.10',
    description="A pyjan26 plugin to generate dynamic sitemaps",
    author="Josnin",
    license="MIT",
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Source': 'https://github.com/josnin/pyjan26-plugins/sitemap',
    }
    )
