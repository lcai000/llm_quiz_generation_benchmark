"""
LLM Framework for Quiz Generation Benchmark
Provides a clean interface for interacting with Google Gemini API.
"""

from .gemini_client import GeminiClient
from .exceptions import LLMFrameworkError, ConfigurationError, APIError

__version__ = "1.0.0"
__all__ = ["GeminiClient", "LLMFrameworkError", "ConfigurationError", "APIError"]