#!/usr/bin/env python3
"""
Setup script for Shazam CLI tool
"""

from setuptools import setup, find_packages
import os

def read_requirements():
    """Read requirements from requirements.txt"""
    requirements_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(requirements_path):
        with open(requirements_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name="shazam-cli",
    version="1.0.0",
    description="AI-powered CLI tool that converts natural language to bash commands",
    author="Sudheesh Shetty",
    author_email="sudheeshshetty48l@gmail.com",
    packages=find_packages(),
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'shazam=shazam.cli:main',
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)