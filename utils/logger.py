"""
Logging utilities for the LLM Quiz Generation Benchmark.
"""
import logging
import sys
from typing import Optional
from pathlib import Path
from config.settings import config


class Logger:
    """Centralized logging configuration."""

    def __init__(self, name: str = "llm_quiz_benchmark"):
        self.logger = logging.getLogger(name)
        self._setup_logger()

    def _setup_logger(self) -> None:
        """Set up the logger with appropriate handlers and formatters."""
        # Clear existing handlers
        self.logger.handlers.clear()

        # Set log level
        level = getattr(logging, config.log_level.upper(), logging.INFO)
        self.logger.setLevel(level)

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # File handler
        log_dir = Path(config.output_dir) / "logs"
        log_dir.mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_dir / "quiz_benchmark.log")
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def debug(self, message: str, **kwargs) -> None:
        """Log debug message."""
        self.logger.debug(message, **kwargs)

    def info(self, message: str, **kwargs) -> None:
        """Log info message."""
        self.logger.info(message, **kwargs)

    def warning(self, message: str, **kwargs) -> None:
        """Log warning message."""
        self.logger.warning(message, **kwargs)

    def error(self, message: str, **kwargs) -> None:
        """Log error message."""
        self.logger.error(message, **kwargs)

    def critical(self, message: str, **kwargs) -> None:
        """Log critical message."""
        self.logger.critical(message, **kwargs)


# Global logger instance
logger = Logger().logger