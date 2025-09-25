"""
Google Gemini API client with improved error handling and logging.
"""
import os
import requests
from typing import Optional, Dict, Any
from .exceptions import ConfigurationError, APIError, ValidationError


class GeminiClient:
    """Google Gemini API client with proper error handling and validation."""

    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None, api_url: Optional[str] = None):
        """
        Initialize Gemini client.

        Args:
            api_key: Gemini API key (falls back to env var LLM_KEY)
            model_name: Model name (falls back to env var LLM_NAME)
            api_url: API URL (falls back to env var LLM_URL)
        """
        self.api_key = api_key or os.getenv('LLM_KEY')
        self.model_name = model_name or os.getenv('LLM_NAME', 'gemini-2.5-flash-lite')
        self.api_url = api_url or os.getenv('LLM_URL')

        self._validate_config()

    def _validate_config(self) -> None:
        """Validate client configuration."""
        if not self.api_key:
            raise ConfigurationError("Gemini API key is required. Set LLM_KEY environment variable or pass api_key parameter.")
        if not self.model_name:
            raise ConfigurationError("Model name is required. Set LLM_NAME environment variable or pass model_name parameter.")
        if not self.api_url:
            raise ConfigurationError("API URL is required. Set LLM_URL environment variable or pass api_url parameter.")

    def _validate_request(self, prompt: str) -> None:
        """Validate request parameters."""
        if not prompt or not prompt.strip():
            raise ValidationError("Prompt cannot be empty")

    def _prepare_request_data(self, prompt: str, system_prompt: Optional[str] = None, max_tokens: Optional[int] = None) -> Dict[str, Any]:
        """Prepare request data for Gemini API."""
        # Combine system prompt with user prompt if provided
        if system_prompt:
            prompt = f"{system_prompt}\n\nUser Question: {prompt}"

        data = {
            "contents": [
                {"role": "user", "parts": [{"text": prompt}]}
            ]
        }

        # Add generation configuration if specified
        if max_tokens:
            data["generationConfig"] = {"maxOutputTokens": max_tokens}

        return data

    def _prepare_headers(self) -> Dict[str, str]:
        """Prepare headers for Gemini API."""
        return {
            "x-goog-api-key": self.api_key,
            "Content-Type": "application/json",
        }

    def _parse_response(self, response_data: Dict[str, Any]) -> str:
        """Parse Gemini API response."""
        try:
            if "candidates" not in response_data or not response_data["candidates"]:
                raise APIError("No candidates in response - prompt may have been blocked by safety settings")

            candidate = response_data["candidates"][0]
            if "content" not in candidate or "parts" not in candidate["content"]:
                raise APIError("Invalid candidate format in response")

            return str(candidate["content"]["parts"][0]["text"])

        except KeyError as e:
            raise APIError(f"Error parsing Gemini response: {e}")

    def generate_response(self, prompt: str, system_prompt: Optional[str] = None, max_tokens: Optional[int] = None) -> str:
        """
        Generate response from Gemini API.

        Args:
            prompt: The user prompt
            system_prompt: Optional system prompt
            max_tokens: Optional maximum tokens for response

        Returns:
            Generated text response

        Raises:
            ValidationError: If input validation fails
            APIError: If API call fails
            ConfigurationError: If configuration is invalid
        """
        self._validate_request(prompt)

        try:
            data = self._prepare_request_data(prompt, system_prompt, max_tokens)
            headers = self._prepare_headers()

            response = requests.post(self.api_url, json=data, headers=headers)
            response.raise_for_status()

            response_data = response.json()
            return self._parse_response(response_data)

        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP Error: {e}\nResponse Content: {e.response.text}"
            raise APIError(error_msg)
        except (ValidationError, ConfigurationError):
            raise
        except Exception as e:
            raise APIError(f"Unexpected error with Gemini API: {e}")

    # Backward compatibility method
    def get_output(self, prompt: str, system_prompt: Optional[str] = None, max_tokens: Optional[int] = None) -> str:
        """Alias for generate_response for backward compatibility."""
        return self.generate_response(prompt, system_prompt, max_tokens)