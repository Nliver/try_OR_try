"""
Setup script for try_or_try package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="try_or_try",
    version="1.0.0",
    author="Nliver",
    description="A simple utility for chaining fallback operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nliver/try_OR_try",
    py_modules=["try_or_try"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    test_suite="test_try_or_try",
)
