"""
Base classes for benchmark-focused prompt generation.
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging


@dataclass
class BenchmarkPrompt:
    """Represents a benchmark prompt set with metadata."""
    user_prompt: str
    system_prompt: str
    subject: str
    topic: str
    expected_difficulty: str
    question_count: int
    quality_metrics: Dict[str, Any]


class BaseBenchmarkGenerator(ABC):
    """Abstract base class for benchmark prompt generators."""

    def __init__(self, subject: str, logger: Optional[logging.Logger] = None):
        """
        Initialize the benchmark generator.

        Args:
            subject: Subject area (e.g., "Algebra", "Biology")
            logger: Optional logger instance
        """
        self.subject = subject
        self.logger = logger or logging.getLogger(f"{subject}Benchmark")
        self._setup_templates()

    @abstractmethod
    def _setup_templates(self) -> None:
        """Set up prompt templates for the specific subject."""
        pass

    def generate_benchmark_prompt(self, topic: str, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """
        Generate a benchmark prompt for LLM evaluation.

        Args:
            topic: Specific topic within the subject
            question_count: Number of questions to generate
            **kwargs: Additional topic-specific parameters

        Returns:
            Benchmark prompt set with metadata
        """
        if question_count <= 0:
            raise ValueError("Question count must be greater than 0")

        # Get topic-specific templates
        user_template, system_template = self._get_topic_templates(topic)

        # Generate prompts
        user_prompt = self._fill_template(user_template, {
            'quantity': question_count,
            'topic': topic,
            **kwargs
        })

        system_prompt = self._fill_template(system_template, {
            'quantity': question_count,
            'topic': topic,
            **kwargs
        })

        # Create quality metrics
        quality_metrics = self._define_quality_metrics(topic)

        self.logger.info(f"Generated {self.subject} benchmark prompt for {topic}: {question_count} questions")
        self.logger.debug(f"Quality metrics: {quality_metrics}")

        return BenchmarkPrompt(
            user_prompt=user_prompt.strip(),
            system_prompt=system_prompt.strip(),
            subject=self.subject,
            topic=topic,
            expected_difficulty="Challenging High School",
            question_count=question_count,
            quality_metrics=quality_metrics
        )

    @abstractmethod
    def _get_topic_templates(self, topic: str) -> tuple:
        """Get user and system templates for a specific topic."""
        pass

    def _fill_template(self, template: str, variables: Dict[str, Any]) -> str:
        """Fill template with variables."""
        try:
            return template.format(**variables)
        except KeyError as e:
            raise ValueError(f"Missing variable in template: {e}")

    def _define_quality_metrics(self, topic: str) -> Dict[str, Any]:
        """Define quality metrics for evaluating LLM responses."""
        return {
            'accuracy_weight': 0.4,
            'clarity_weight': 0.2,
            'difficulty_weight': 0.2,
            'educational_value_weight': 0.2,
            'expected_complexity': 'High',
            'grading_criteria': self._get_grading_criteria(topic)
        }

    def _get_grading_criteria(self, topic: str) -> List[str]:
        """Get specific grading criteria for the topic."""
        return [
            "Mathematical accuracy",
            "Clear problem statement",
            "Appropriate difficulty level",
            "Educational relevance",
            "Unambiguous correct answer"
        ]

    def list_topics(self) -> List[str]:
        """List all available topics for this subject."""
        return list(self._get_topic_templates('').keys()) if hasattr(self, '_topic_templates') else []

    def generate_comprehensive_benchmark(self, questions_per_topic: int = 5) -> List[BenchmarkPrompt]:
        """Generate benchmark prompts for all topics in the subject."""
        all_prompts = []
        topics = self.list_topics()

        for topic in topics:
            try:
                prompt = self.generate_benchmark_prompt(topic, questions_per_topic)
                all_prompts.append(prompt)
            except Exception as e:
                self.logger.error(f"Failed to generate prompt for {topic}: {e}")
                continue

        return all_prompts