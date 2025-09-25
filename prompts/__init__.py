"""
Comprehensive benchmark prompt generation system for LLM evaluation.
This module provides structured prompt generation for testing LLM question quality.
"""

from .base import BenchmarkPrompt, BaseBenchmarkGenerator
from .benchmark_manager import BenchmarkManager, BenchmarkSuite, benchmark_manager
from .math.algebra import AlgebraBenchmark
from .math.precalculus import PrecalculusBenchmark
from .science.biology import BiologyBenchmark
from .science.chemistry import ChemistryBenchmark
from .history.us_history import USHistoryBenchmark
from .history.world_history import WorldHistoryBenchmark
from .programming.java import JavaBenchmark

__all__ = [
    'BenchmarkPrompt',
    'BaseBenchmarkGenerator',
    'BenchmarkManager',
    'BenchmarkSuite',
    'benchmark_manager',
    'AlgebraBenchmark',
    'PrecalculusBenchmark',
    'BiologyBenchmark',
    'ChemistryBenchmark',
    'USHistoryBenchmark',
    'WorldHistoryBenchmark',
    'JavaBenchmark'
]