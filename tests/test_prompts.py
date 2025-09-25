"""
Unit tests for prompt generation functionality.
"""
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prompts import PromptGenerator, MathQuizGenerator, ValidationError, QuizPrompt
from llm_framework import LLM


class TestPromptGenerator(unittest.TestCase):
    """Test cases for PromptGenerator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.generator = PromptGenerator(delimiter="|")

    def test_valid_quiz_prompt_generation(self):
        """Test generation of valid quiz prompts."""
        prompt_set = self.generator.generate_quiz_prompt(
            quantity=5,
            details="Math quiz for 5th graders"
        )

        self.assertIsInstance(prompt_set, QuizPrompt)
        self.assertIn("5 questions", prompt_set.user_prompt)
        self.assertIn("Math quiz for 5th graders", prompt_set.user_prompt)
        self.assertIn("Expert Quiz Creator", prompt_set.system_prompt)
        self.assertEqual(prompt_set.metadata["quantity"], 5)

    def test_invalid_quantity_validation(self):
        """Test validation of invalid quantity."""
        with self.assertRaises(ValidationError):
            self.generator.generate_quiz_prompt(quantity=0, details="test")

        with self.assertRaises(ValidationError):
            self.generator.generate_quiz_prompt(quantity=-5, details="test")

    def test_empty_details_validation(self):
        """Test validation of empty details."""
        with self.assertRaises(ValidationError):
            self.generator.generate_quiz_prompt(quantity=5, details="")

        with self.assertRaises(ValidationError):
            self.generator.generate_quiz_prompt(quantity=5, details="   ")

    def test_backward_compatibility_call(self):
        """Test backward compatibility __call__ method."""
        result = self.generator(quantity=5, details="Math quiz")

        self.assertIsInstance(result, dict)
        self.assertIn("user_prompt", result)
        self.assertIn("system_prompt", result)
        self.assertIn("5 questions", result["user_prompt"])


class TestMathQuizGenerator(unittest.TestCase):
    """Test cases for MathQuizGenerator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.math_generator = MathQuizGenerator()

    def test_multiplication_prompt_generation(self):
        """Test multiplication quiz prompt generation."""
        result = self.math_generator.multiplication(
            quantity=3,
            grade_level="6th-7th",
            digits="2 digit by 2 digit"
        )

        self.assertIsInstance(result, dict)
        self.assertIn("user_prompt", result)
        self.assertIn("system_prompt", result)
        self.assertIn("3 questions", result["user_prompt"])
        self.assertIn("2 digit by 2 digit", result["user_prompt"])
        self.assertIn("6th-7th", result["user_prompt"])

    def test_algebraic_equations_prompt_generation(self):
        """Test algebraic equations prompt generation."""
        result = self.math_generator.algebraic_equations(
            quantity=5,
            grade_level="8th-9th",
            complexity="advanced operations"
        )

        self.assertIsInstance(result, dict)
        self.assertIn("5 questions", result["user_prompt"])
        self.assertIn("algebraic equations", result["user_prompt"])
        self.assertIn("advanced operations", result["user_prompt"])
        self.assertIn("8th-9th", result["user_prompt"])

    def test_fractions_prompt_generation(self):
        """Test fractions prompt generation."""
        result = self.math_generator.fractions(
            quantity=4,
            grade_level="5th-6th",
            operations="addition and subtraction"
        )

        self.assertIsInstance(result, dict)
        self.assertIn("4 questions", result["user_prompt"])
        self.assertIn("fractions", result["user_prompt"])
        self.assertIn("addition and subtraction", result["user_prompt"])
        self.assertIn("5th-6th", result["user_prompt"])

    def test_default_parameters(self):
        """Test default parameter values."""
        result = self.math_generator.multiplication()

        self.assertIn("10 questions", result["user_prompt"])
        self.assertIn("3rd-4th", result["user_prompt"])
        self.assertIn("3 digit by 3 digit", result["user_prompt"])


class TestBackwardCompatibility(unittest.TestCase):
    """Test cases for backward compatibility classes."""

    def test_generate_prompts_class(self):
        """Test GeneratePrompts backward compatibility class."""
        from prompts import GeneratePrompts

        with patch('os.getenv', return_value='|'):
            generator = GeneratePrompts()
            result = generator("Create a 5 question math quiz for 6th graders")

            self.assertIsInstance(result, dict)
            self.assertIn("user_prompt", result)
            self.assertIn("system_prompt", result)

    def test_math_class(self):
        """Test Math backward compatibility class."""
        from prompts import Math

        math_gen = Math()
        math_gen.quantity = 5

        result = math_gen.multiplication()

        self.assertIsInstance(result, dict)
        self.assertIn("user_prompt", result)
        self.assertIn("system_prompt", result)

    def test_math_class_algebra(self):
        """Test Math class algebraic equations method."""
        from prompts import Math

        math_gen = Math()
        math_gen.quantity = 3

        result = math_gen.algebraic_equations()

        self.assertIsInstance(result, dict)
        self.assertIn("user_prompt", result)
        self.assertIn("system_prompt", result)
        self.assertIn("algebraic equations", result["user_prompt"])


if __name__ == '__main__':
    unittest.main()