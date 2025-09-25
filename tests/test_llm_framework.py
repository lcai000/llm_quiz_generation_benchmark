"""
Unit tests for LLM framework functionality.
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_framework import GeminiClient, ConfigurationError, APIError, ValidationError


class TestGeminiClient(unittest.TestCase):
    """Test cases for GeminiClient class."""

    def setUp(self):
        """Set up test fixtures."""
        self.api_key = "test_api_key"
        self.model_name = "test_model"
        self.api_url = "https://test.googleapis.com/v1/models/test_model:generateContent"

    def test_initialization_with_params(self):
        """Test initialization with parameters."""
        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        self.assertEqual(client.api_key, self.api_key)
        self.assertEqual(client.model_name, self.model_name)
        self.assertEqual(client.api_url, self.api_url)

    @patch('os.getenv')
    def test_initialization_with_env_vars(self, mock_getenv):
        """Test initialization with environment variables."""
        mock_getenv.side_effect = lambda key, default=None: {
            'LLM_KEY': self.api_key,
            'LLM_NAME': self.model_name,
            'LLM_URL': self.api_url
        }.get(key, default)

        client = GeminiClient()

        self.assertEqual(client.api_key, self.api_key)
        self.assertEqual(client.model_name, self.model_name)
        self.assertEqual(client.api_url, self.api_url)

    def test_missing_api_key_validation(self):
        """Test validation of missing API key."""
        with self.assertRaises(ConfigurationError):
            GeminiClient(api_key="", model_name=self.model_name, api_url=self.api_url)

        with self.assertRaises(ConfigurationError):
            GeminiClient(api_key=None, model_name=self.model_name, api_url=self.api_url)

    def test_missing_model_name_validation(self):
        """Test validation of missing model name."""
        with self.assertRaises(ConfigurationError):
            GeminiClient(api_key=self.api_key, model_name="", api_url=self.api_url)

    def test_missing_api_url_validation(self):
        """Test validation of missing API URL."""
        with self.assertRaises(ConfigurationError):
            GeminiClient(api_key=self.api_key, model_name=self.model_name, api_url="")

    def test_empty_prompt_validation(self):
        """Test validation of empty prompt."""
        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        with self.assertRaises(ValidationError):
            client.generate_response(prompt="")

        with self.assertRaises(ValidationError):
            client.generate_response(prompt="   ")

    @patch('requests.post')
    def test_successful_api_call(self, mock_post):
        """Test successful API call."""
        # Mock successful response
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": "Generated quiz content"}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        result = client.generate_response(
            prompt="Generate a math quiz",
            system_prompt="You are a math teacher"
        )

        self.assertEqual(result, "Generated quiz content")
        mock_post.assert_called_once()

        # Check request structure
        call_args = mock_post.call_args
        self.assertEqual(call_args[1]['headers']['x-goog-api-key'], self.api_key)
        self.assertEqual(call_args[1]['headers']['Content-Type'], 'application/json')

    @patch('requests.post')
    def test_api_call_with_max_tokens(self, mock_post):
        """Test API call with max tokens parameter."""
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": "Generated content"}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        result = client.generate_response(
            prompt="Generate a quiz",
            max_tokens=1000
        )

        self.assertEqual(result, "Generated content")

        # Check that max tokens was included in request
        call_args = mock_post.call_args
        payload = call_args[1]['json']
        self.assertIn('generationConfig', payload)
        self.assertEqual(payload['generationConfig']['maxOutputTokens'], 1000)

    @patch('requests.post')
    def test_api_call_http_error(self, mock_post):
        """Test API call with HTTP error."""
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("HTTP 400 Bad Request")
        mock_response.text = "Error details"
        mock_post.return_value = mock_response

        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        with self.assertRaises(APIError):
            client.generate_response(prompt="Generate a quiz")

    @patch('requests.post')
    def test_api_call_no_candidates(self, mock_post):
        """Test API call with no candidates in response."""
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "candidates": []
        }
        mock_post.return_value = mock_response

        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        with self.assertRaises(APIError):
            client.generate_response(prompt="Generate a quiz")

    @patch('requests.post')
    def test_api_call_malformed_response(self, mock_post):
        """Test API call with malformed response."""
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        # Missing parts
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        with self.assertRaises(APIError):
            client.generate_response(prompt="Generate a quiz")

    @patch('requests.post')
    def test_generate_simple_method(self, mock_post):
        """Test generate_simple method."""
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "candidates": [
                {
                    "content": {
                        "parts": [
                            {"text": "Simple response"}
                        ]
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        client = GeminiClient(
            api_key=self.api_key,
            model_name=self.model_name,
            api_url=self.api_url
        )

        result = client.generate_simple("Simple prompt")
        self.assertEqual(result, "Simple response")


class TestLLMLegacyClasses(unittest.TestCase):
    """Test cases for legacy LLM classes."""

    def test_llm_class_initialization(self):
        """Test LLM class initialization."""
        from llm_framework import LLM

        llm = LLM()
        self.assertIsNotNone(llm)

    @patch('os.getenv')
    def test_llm_initialization_success(self, mock_getenv):
        """Test LLM initialization with valid environment variables."""
        from llm_framework import LLM

        mock_getenv.side_effect = lambda key, default=None: {
            'LLM_KEY': 'test_key',
            'LLM_NAME': 'test_model',
            'LLM_URL': 'test_url'
        }.get(key, default)

        llm = LLM()
        key, name, url = llm.initialize_llm('LLM_KEY', 'LLM_NAME', 'LLM_URL')

        self.assertEqual(key, 'test_key')
        self.assertEqual(name, 'test_model')
        self.assertEqual(url, 'test_url')

    @patch('os.getenv')
    def test_llm_initialization_missing_env_var(self, mock_getenv):
        """Test LLM initialization with missing environment variable."""
        from llm_framework import LLM, ConfigurationError

        mock_getenv.return_value = None

        llm = LLM()
        with self.assertRaises(ConfigurationError):
            llm.initialize_llm('MISSING_KEY', 'LLM_NAME', 'LLM_URL')

    def test_llm_agent_method(self):
        """Test LLM agent method."""
        from llm_framework import LLM

        llm = LLM()
        agent_prompt = llm.agent(
            identity="Test Agent",
            purpose="Test Purpose",
            output_style="Test Style"
        )

        self.assertIn("Test Agent", agent_prompt)
        self.assertIn("Test Purpose", agent_prompt)
        self.assertIn("Test Style", agent_prompt)


if __name__ == '__main__':
    unittest.main()