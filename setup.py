from setuptools import setup, find_packages # type: ignore

setup(
    name="test-python-app",
    version="0.1.0",
    description="A test Python app",
    author="Your Name",
    packages=find_packages(include=["app", "app.*"]),
    install_requires=[],
)