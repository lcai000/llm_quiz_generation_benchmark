"""
Prompt generation utilities for quiz creation with improved structure and validation.
"""
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import logging

from exceptions import ValidationError
from llm_framework import LLM


@dataclass
class PromptTemplate:
    """Template for generating prompts."""
    template: str
    required_vars: List[str]
    optional_vars: Dict[str, Any] = None


@dataclass
class QuizPrompt:
    """Represents a complete quiz prompt set."""
    user_prompt: str
    system_prompt: str
    metadata: Dict[str, Any]


class PromptGenerator:
    """
    Generates prompts for LLM quiz creation with proper validation.
    """

    def __init__(self, delimiter: str = "|"):
        """
        Initialize prompt generator.

        Args:
            delimiter: Delimiter for quiz format
        """
        self.delimiter = delimiter
        self.llm = LLM()
        self.logger = logging.getLogger(__name__)

        # Define prompt templates
        self._setup_templates()

    def _setup_templates(self) -> None:
        """Set up prompt templates."""
        self.templates = {
            'user_quiz': PromptTemplate(
                template="""
Generate a multiple-choice quiz based on the following details.

Requirements:
- Generate exactly {quantity} questions
- Each question must have 4 answer choices
- No blank lines in the output
- No labels, only content
- Questions should contain only the question text, no answers
- Use the exact format specified below

Output format for each question:
{delimiter_example}

Quiz details:
{details}

Remember: Follow the format exactly and generate {quantity} questions.
""",
                required_vars=['quantity', 'details'],
                optional_vars={'delimiter_example': f"question {self.delimiter} correct_answer {self.delimiter} incorrect1 {self.delimiter} incorrect2 {self.delimiter} incorrect3"}
            ),
            'system_quiz_agent': PromptTemplate(
                template=self.llm.agent(
                    identity="Expert Quiz Creator",
                    purpose="Create accurate, educational, and engaging multiple-choice quizzes",
                    output_style="follow formatting instructions precisely",
                    agent_context="Educational AI assistant specializing in quiz creation",
                    notes="Always double-check mathematical calculations and ensure questions are age-appropriate"
                ),
                required_vars=[],
                optional_vars={}
            )
        }

    def _validate_template_vars(self, template: PromptTemplate, variables: Dict[str, Any]) -> None:
        """Validate that all required variables are provided."""
        missing_vars = []
        for var in template.required_vars:
            if var not in variables:
                missing_vars.append(var)

        if missing_vars:
            raise ValidationError(f"Missing required variables for template: {missing_vars}")

    def _fill_template(self, template: PromptTemplate, variables: Dict[str, Any]) -> str:
        """Fill template with variables."""
        self._validate_template_vars(template, variables)

        # Combine required and optional variables
        all_vars = template.optional_vars.copy() if template.optional_vars else {}
        all_vars.update(variables)

        try:
            return template.template.format(**all_vars)
        except KeyError as e:
            raise ValidationError(f"Missing variable in template: {e}")

    def generate_quiz_prompt(self, quantity: int, details: str) -> QuizPrompt:
        """
        Generate a complete quiz prompt set.

        Args:
            quantity: Number of questions to generate
            details: Details about the quiz topic and requirements

        Returns:
            Complete quiz prompt set

        Raises:
            ValidationError: If input validation fails
        """
        try:
            if quantity <= 0:
                raise ValidationError("Quantity must be greater than 0")

            if not details or not details.strip():
                raise ValidationError("Quiz details cannot be empty")

            # Generate user prompt
            user_prompt = self._fill_template(
                self.templates['user_quiz'],
                {
                    'quantity': quantity,
                    'details': details,
                    'delimiter_example': f"question {self.delimiter} correct_answer {self.delimiter} incorrect1 {self.delimiter} incorrect2 {self.delimiter} incorrect3"
                }
            )

            # Generate system prompt
            system_prompt = self._fill_template(
                self.templates['system_quiz_agent'],
                {}
            )

            # Create metadata
            metadata = {
                'quantity': quantity,
                'details': details,
                'delimiter': self.delimiter,
                'template': 'quiz'
            }

            self.logger.info(f"Generated quiz prompt for {quantity} questions")
            self.logger.debug(f"Details: {details}")

            return QuizPrompt(
                user_prompt=user_prompt.strip(),
                system_prompt=system_prompt.strip(),
                metadata=metadata
            )

        except Exception as e:
            self.logger.error(f"Failed to generate quiz prompt: {e}")
            raise ValidationError(f"Prompt generation failed: {e}")

    def __call__(self, quantity: int, details: str) -> Dict[str, str]:
        """
        Generate prompts for backward compatibility.

        Args:
            quantity: Number of questions
            details: Quiz details

        Returns:
            Dictionary with user_prompt and system_prompt
        """
        prompt_set = self.generate_quiz_prompt(quantity, details)
        return {
            "user_prompt": prompt_set.user_prompt,
            "system_prompt": prompt_set.system_prompt
        }


class MathQuizGenerator:
    """
    Specialized prompt generator for math quizzes.
    """

    def __init__(self):
        """Initialize math quiz generator."""
        self.prompt_generator = PromptGenerator()
        self.logger = logging.getLogger(__name__)

    def multiplication(self, quantity: int = 10, grade_level: str = "3rd-4th", digits: str = "3 digit by 3 digit") -> Dict[str, str]:
        """
        Generate multiplication quiz prompts.

        Args:
            quantity: Number of questions
            grade_level: Target grade level
            digits: Number of digits in multiplication problems

        Returns:
            Dictionary with user_prompt and system_prompt
        """
        details = f"Create a {quantity} question {digits} multiplication quiz for {grade_level} graders. Questions should be age-appropriate and cover various multiplication scenarios."
        return self.prompt_generator(quantity, details)

    def algebraic_equations(self, quantity: int = 10, grade_level: str = "5th-6th", complexity: str = "multiple operations") -> Dict[str, str]:
        """
        Generate algebraic equations quiz prompts.

        Args:
            quantity: Number of questions
            grade_level: Target grade level
            complexity: Complexity level of equations

        Returns:
            Dictionary with user_prompt and system_prompt
        """
        details = f"Create a {quantity} question algebraic equations with {complexity}, for {grade_level} graders. Include various types of equations like linear equations, equations with variables on both sides, and word problems."
        return self.prompt_generator(quantity, details)

    def fractions(self, quantity: int = 10, grade_level: str = "4th-5th", operations: str = "addition, subtraction, multiplication") -> Dict[str, str]:
        """
        Generate fractions quiz prompts.

        Args:
            quantity: Number of questions
            grade_level: Target grade level
            operations: Types of operations to include

        Returns:
            Dictionary with user_prompt and system_prompt
        """
        details = f"Create a {quantity} question fractions quiz covering {operations} for {grade_level} graders. Include proper fractions, improper fractions, and mixed numbers."
        return self.prompt_generator(quantity, details)


# Backward compatibility classes
class GeneratePrompts:
    """Legacy class for backward compatibility."""

    def __init__(self):
        """Initialize with environment delimiter."""
        from dotenv import load_dotenv
        load_dotenv(override=True)
        self.delimiter = os.getenv('DELIMETER', '|')
        self.generator = PromptGenerator(delimiter=self.delimiter)

    def _user_prompt(self, details: str) -> str:
        """Generate user prompt (legacy method)."""
        # Extract quantity from details if possible
        quantity = 10  # Default
        if "Create a" in details and "question" in details:
            try:
                # Simple extraction - this could be improved
                words = details.split()
                for i, word in enumerate(words):
                    if word.isdigit():
                        quantity = int(word)
                        break
            except:
                pass

        prompt_set = self.generator.generate_quiz_prompt(quantity, details)
        return prompt_set.user_prompt

    def _system_prompt(self) -> str:
        """Generate system prompt (legacy method)."""
        prompt_set = self.generator.generate_quiz_prompt(10, "quiz")
        return prompt_set.system_prompt

    def __call__(self, details: str) -> Dict[str, str]:
        """Generate prompts (legacy method)."""
        quantity = 10  # Default
        if "Create a" in details and "question" in details:
            try:
                words = details.split()
                for i, word in enumerate(words):
                    if word.isdigit():
                        quantity = int(word)
                        break
            except:
                pass

        return self.generator(quantity, details)


class Math:
    """Legacy class for backward compatibility."""

    def __init__(self):
        """Initialize math quiz generator."""
        self.math_generator = MathQuizGenerator()
        self.quantity: int = 10

    def multiplication(self) -> Dict[str, str]:
        """Generate multiplication quiz prompts."""
        return self.math_generator.multiplication(quantity=self.quantity)

    def algebraic_equations(self) -> Dict[str, str]:
        """Generate algebraic equations quiz prompts."""
        return self.math_generator.algebraic_equations(quantity=self.quantity)


if __name__ == "__main__":
    # Example usage
    math_gen = MathQuizGenerator()

    # Generate multiplication prompts
    mult_prompts = math_gen.multiplication(quantity=5, grade_level="4th-5th")
    print("Multiplication Quiz Prompts:")
    print("User Prompt:")
    print(mult_prompts["user_prompt"])
    print("\nSystem Prompt:")
    print(mult_prompts["system_prompt"])

    # Generate algebra prompts
    alg_prompts = math_gen.algebraic_equations(quantity=3, grade_level="6th-7th")
    print("\n\nAlgebraic Equations Quiz Prompts:")
    print("User Prompt:")
    print(alg_prompts["user_prompt"])
    print("\nSystem Prompt:")
    print(alg_prompts["system_prompt"])