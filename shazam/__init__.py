#!/usr/bin/env python3
"""
Shazam - AI-powered CLI tool for converting natural language to bash commands
"""

__version__ = "1.0.0"
__author__ = "Sudheesh Shetty"
__email__ = "sudheeshshetty48@gmail.com"

from .config import Config
from .model import ModelInterface
from .cli import main

__all__ = ['Config', 'ModelInterface', 'main']