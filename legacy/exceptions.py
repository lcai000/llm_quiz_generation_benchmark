"""
Custom exceptions for the LLM Quiz Generation Benchmark.
"""


class QuizGenerationError(Exception):
    """Base exception for quiz generation errors."""
    pass


class LLMConfigurationError(QuizGenerationError):
    """Exception raised when LLM configuration is invalid."""
    pass


class LLMAPICallError(QuizGenerationError):
    """Exception raised when LLM API call fails."""
    pass


class QuizFormatError(QuizGenerationError):
    """Exception raised when quiz formatting fails."""
    pass


class ValidationError(QuizGenerationError):
    """Exception raised when input validation fails."""
    pass