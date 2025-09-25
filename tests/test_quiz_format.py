"""
Unit tests for quiz formatting functionality.
"""
import unittest
import json
from unittest.mock import patch, MagicMock
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quiz_format import QuizFormatter, QuizQuestion, ValidationError, QuizFormatError


class TestQuizFormatter(unittest.TestCase):
    """Test cases for QuizFormatter class."""

    def setUp(self):
        """Set up test fixtures."""
        self.formatter = QuizFormatter(delimiter="|", shuffle_choices=False)
        self.sample_questions = """
What is 2 + 2? | 4 | 3 | 5 | 6
What is 3 × 4? | 12 | 10 | 15 | 8
What is 10 ÷ 2? | 5 | 2 | 3 | 6
"""

    def test_valid_questions_formatting(self):
        """Test formatting of valid questions."""
        result = self.formatter.format_questions(self.sample_questions)

        self.assertEqual(len(result), 3)
        self.assertIn("0", result)
        self.assertIn("1", result)
        self.assertIn("2", result)

        # Check first question structure
        q0 = result["0"]
        self.assertIn("QUESTION", q0)
        self.assertIn("ANSWER", q0)
        self.assertIn("CHOICES", q0)
        self.assertEqual(len(q0["CHOICES"]), 4)

    def test_empty_input_validation(self):
        """Test validation of empty input."""
        with self.assertRaises(ValidationError):
            self.formatter.format_questions("")

        with self.assertRaises(ValidationError):
            self.formatter.format_questions("   \n   \n   ")

    def test_malformed_questions(self):
        """Test handling of malformed questions."""
        malformed = """
What is 2 + 2? | 4 | 3 | 5
Invalid question with no answers
What is 3 × 4? | 12 | 10 | 15 | 8
"""

        # Should handle gracefully and format valid questions
        result = self.formatter.format_questions(malformed)
        self.assertEqual(len(result), 2)  # Only valid questions

    def test_single_choice_question(self):
        """Test question with only one choice."""
        single_choice = "What is 1 + 1? | 2"
        result = self.formatter.format_questions(single_choice)

        self.assertEqual(len(result), 1)
        q0 = result["0"]
        self.assertEqual(len(q0["CHOICES"]), 1)
        self.assertEqual(q0["ANSWER"], 0)

    def test_json_output(self):
        """Test JSON output formatting."""
        json_result = self.formatter.format_to_json(self.sample_questions)
        self.assertIsInstance(json_result, str)

        # Should be valid JSON
        parsed = json.loads(json_result)
        self.assertEqual(len(parsed), 3)

    def test_custom_delimiter(self):
        """Test with custom delimiter."""
        custom_formatter = QuizFormatter(delimiter="#")
        custom_questions = "What is 2 + 2? # 4 # 3 # 5 # 6"

        result = custom_formatter.format_questions(custom_questions)
        self.assertEqual(len(result), 1)
        self.assertEqual(result["0"]["CHOICES"][0], "4")

    @patch('builtins.open', create=True)
    def test_save_to_file(self, mock_open):
        """Test saving to file."""
        mock_file = MagicMock()
        mock_open.return_value.__enter__.return_value = mock_file

        self.formatter.save_to_file(self.sample_questions, "test_output.json")
        mock_open.assert_called_once_with("test_output.json", 'w', encoding='utf-8')
        mock_file.write.assert_called_once()

    def test_backward_compatibility_function(self):
        """Test backward compatibility function."""
        from quiz_format import format_question

        with patch('os.getenv', return_value='|'):
            result = format_question(self.sample_questions)
            self.assertIsInstance(result, str)

            # Should be valid JSON
            parsed = json.loads(result)
            self.assertEqual(len(parsed), 3)


class TestQuizQuestion(unittest.TestCase):
    """Test cases for QuizQuestion dataclass."""

    def test_quiz_question_creation(self):
        """Test QuizQuestion dataclass creation."""
        question = QuizQuestion(
            question="What is 2 + 2?",
            answer="4",
            choices=["4", "3", "5", "6"],
            correct_index=0
        )

        self.assertEqual(question.question, "What is 2 + 2?")
        self.assertEqual(question.answer, "4")
        self.assertEqual(len(question.choices), 4)
        self.assertEqual(question.correct_index, 0)


if __name__ == '__main__':
    unittest.main()