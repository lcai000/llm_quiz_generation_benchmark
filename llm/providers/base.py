"""
Base classes for LLM providers.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from dataclasses import dataclass


@dataclass
class LLMRequest:
    """Represents a request to an LLM."""
    prompt: str
    system_prompt: Optional[str] = None
    max_tokens: Optional[int] = None
    temperature: float = 0.7
    additional_params: Optional[Dict[str, Any]] = None


@dataclass
class LLMResponse:
    """Represents a response from an LLM."""
    content: str
    model: str
    usage: Optional[Dict[str, Any]] = None
    raw_response: Optional[Dict[str, Any]] = None


class LLMProvider(ABC):
    """Abstract base class for LLM providers."""

    def __init__(self, api_key: str, model_name: str, api_url: str):
        self.api_key = api_key
        self.model_name = model_name
        self.api_url = api_url

    @abstractmethod
    def prepare_request(self, request: LLMRequest) -> Dict[str, Any]:
        """Prepare the request payload for the API."""
        pass

    @abstractmethod
    def prepare_headers(self) -> Dict[str, str]:
        """Prepare the headers for the API request."""
        pass

    @abstractmethod
    def parse_response(self, response_data: Dict[str, Any]) -> LLMResponse:
        """Parse the API response."""
        pass

    @abstractmethod
    def handle_error(self, error: Exception) -> str:
        """Handle API errors."""
        pass

    def validate_request(self, request: LLMRequest) -> None:
        """Validate the request before sending."""
        if not request.prompt.strip():
            raise ValueError("Prompt cannot be empty")
        if not self.api_key:
            raise ValueError("API key is required")
        if not self.model_name:
            raise ValueError("Model name is required")
        if not self.api_url:
            raise ValueError("API URL is required")