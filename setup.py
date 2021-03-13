from setuptools import find_packages, setup

with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
    name='exaparser',
    version='2021.03.15',
    description='Exabyte Parser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/Exabyte-io/exaparser',
    author='Exabyte Inc.',
    author_email='info@exabyte.io',
    license='Exabyte Inc.',
    packages=find_packages(exclude=['examples', 'docs', 'tests*']),
    install_requires=[
        'exabyte-api-client>=2020.10.19',
        'express-py>=2020.10.19',
        'requests>=2.20.1',
    ],
    extras_require={
        "test": [
            "coverage>=5.3",
            "mock>=1.3.0",
            "numpy>=1.17.3",
        ],
    },
    entry_points={
        'console_scripts': [
            'exaparser=exaparser.cli:main'
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Exabyte Development Team',
        'Topic :: Software Development'
    ],
)
