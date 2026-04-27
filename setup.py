"""Setup configuration for Autoresbot API package."""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='autoresbot-api',
    version='1.0.0',
    description='A Python client for the Autoresbot API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='autorsbot',
    author_email='autoresbot@gmail.com',
    url='https://github.com/yourusername/autoresbot-api',
    packages=find_packages(exclude=['tests', 'examples']),
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.7',
    keywords='autoresbot, api, whatsapp, bot, client',
    project_urls={
        'Documentation': 'https://github.com/yourusername/autoresbot-api/wiki',
        'Source': 'https://github.com/yourusername/autoresbot-api',
        'Bug Reports': 'https://github.com/yourusername/autoresbot-api/issues',
    },
)
