from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="taaontia.py",
    version="0.1.0",
    description="Taaontia game core files",
    long_description=readme,
    author="Kagaminara Shikatsu",
    author_email="",
    url="https://github.com/Kagaminara/taaontia.py",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
