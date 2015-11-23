"""
Descent
=======

A Python package for performing first-order optimization

For more information, see the accompanying README.md

"""

__all__ = [
    'algorithms',
    'connectors',
    'proxops',
    'utils',
    'io',
    'examples',
    ]

from .algorithms import *
from .connectors import *
from .proxops import *
from .utils import *
from .io import *
from .examples import *

__version__ = '0.1.0'
