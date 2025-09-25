"""
Custom exceptions for the LLM Framework.
"""


class LLMFrameworkError(Exception):
    """Base exception for LLM Framework errors."""
    pass


class ConfigurationError(LLMFrameworkError):
    """Exception raised when configuration is invalid."""
    pass


class APIError(LLMFrameworkError):
    """Exception raised when API call fails."""
    pass


class ValidationError(LLMFrameworkError):
    """Exception raised when input validation fails."""
    pass