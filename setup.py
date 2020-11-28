from setuptools import find_packages, setup

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
    name='exaparser',
    version='2020.10.19',
    description='Exabyte Parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/Exabyte-io/exaparser',
    author='Exabyte Inc.',
    author_email='info@exabyte.io',
    license='Exabyte Inc.',
    packages=find_packages(exclude=['examples', 'docs', 'tests*']),
    install_requires=[
        'configparser==3.7.3',
        'esse==2.3.0',
        'exabyte-api-client==1.0.0',
        'express-py==2.6.0',
        'requests==2.20.1',
    ],
    extras_require={
        "test": [
            "coverage>=5.3",
            "mock>=1.3.0",
            "numpy==1.16.4",
        ],
    },
    entry_points={
        'console_scripts': [
            'exaparser=src.cli:main'
        ],
    },
    python_requires='>=2.7,<3',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Exabyte Development Team',
        'Topic :: Software Development'
    ],
)
