from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="funnydeco",
    version="0.1.4",
    author="Vladimir Kirievskiy",
    author_email="vlakir1234@gmail.com",
    description="Collection of useful decorators for various python projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/vlakir/funnydeco/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
