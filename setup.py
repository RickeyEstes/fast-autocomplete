from setuptools import setup, find_packages

version = '0.6.0'


try:
    with open('README.md') as file:
        long_description = file.read()
except Exception:
    long_description = "Autocomplete"

setup(
    name='fast-autocomplete',
    description='Fast Autocomplete using Directed Word Graph',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sep Dehpour',
    url='https://github.com/wearefair/fast-autocomplete',
    author_email='sepd@fair.com',
    version=version,
    install_requires=[],
    extras_require={
        'levenshtein': ['python-Levenshtein>=0.12.0'],
        'pylev': ['pylev>=1.3.0'],
    },
    dependency_links=[],
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    scripts=[],
    test_suite="tests",
    tests_require=['mock'],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 4 - Beta",
    ]
)
