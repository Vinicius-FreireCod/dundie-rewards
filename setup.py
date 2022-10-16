from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description="Reward point System for dunder Mifflin",
    author="Vinicius Freire",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    }
)
