"""
Science benchmark prompt generation modules.
"""

from .biology import BiologyBenchmark
from .chemistry import ChemistryBenchmark

__all__ = [
    'BiologyBenchmark',
    'ChemistryBenchmark'
]