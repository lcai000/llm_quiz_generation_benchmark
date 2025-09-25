"""
Configuration management for LLM Quiz Generation Benchmark.
"""
import os
from typing import Dict, Any, Optional
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class LLMConfig:
    """Configuration for LLM providers."""
    key: str
    name: str
    url: str
    mode: str = "default"
    max_tokens: Optional[int] = None
    temperature: float = 0.7


@dataclass
class QuizConfig:
    """Configuration for quiz generation."""
    default_batch_size: int = 10
    default_quantity: int = 30
    delimiter: str = "|"
    shuffle_choices: bool = True
    max_questions_per_batch: int = 50


@dataclass
class AppConfig:
    """Main application configuration."""
    llm: LLMConfig = field(default_factory=lambda: LLMConfig(
        key=os.getenv("LLM_KEY", ""),
        name=os.getenv("LLM_NAME", "gpt-3.5-turbo"),
        url=os.getenv("LLM_URL", "https://api.openai.com/v1/chat/completions")
    ))
    quiz: QuizConfig = field(default_factory=QuizConfig)
    log_level: str = "INFO"
    output_dir: str = "results"

    def __post_init__(self):
        """Initialize configuration after creation."""
        # Ensure output directory exists
        Path(self.output_dir).mkdir(exist_ok=True)


class ConfigManager:
    """Manages application configuration."""

    def __init__(self):
        self._config = AppConfig()

    @property
    def config(self) -> AppConfig:
        """Get the current configuration."""
        return self._config

    def update_llm_config(self, **kwargs) -> None:
        """Update LLM configuration."""
        for key, value in kwargs.items():
            if hasattr(self._config.llm, key):
                setattr(self._config.llm, key, value)

    def update_quiz_config(self, **kwargs) -> None:
        """Update quiz configuration."""
        for key, value in kwargs.items():
            if hasattr(self._config.quiz, key):
                setattr(self._config.quiz, key, value)

    def load_from_env(self) -> None:
        """Load configuration from environment variables."""
        # LLM Configuration
        self._config.llm.key = os.getenv("LLM_KEY", self._config.llm.key)
        self._config.llm.name = os.getenv("LLM_NAME", self._config.llm.name)
        self._config.llm.url = os.getenv("LLM_URL", self._config.llm.url)
        self._config.llm.mode = os.getenv("LLM_MODE", self._config.llm.mode)

        # Quiz Configuration
        delimiter = os.getenv("DELIMITER")
        if delimiter:
            self._config.quiz.delimiter = delimiter

        batch_size = os.getenv("BATCH_SIZE")
        if batch_size and batch_size.isdigit():
            self._config.quiz.default_batch_size = int(batch_size)

        quantity = os.getenv("QUANTITY")
        if quantity and quantity.isdigit():
            self._config.quiz.default_quantity = int(quantity)

        # App Configuration
        self._config.log_level = os.getenv("LOG_LEVEL", self._config.log_level)
        self._config.output_dir = os.getenv("OUTPUT_DIR", self._config.output_dir)


# Global configuration instance
config_manager = ConfigManager()
config_manager.load_from_env()

# Expose configuration for easy access
config = config_manager.config