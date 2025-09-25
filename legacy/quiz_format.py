"""
Quiz formatting utilities with improved validation and error handling.
"""
import random
import json
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

from exceptions import QuizFormatError, ValidationError


@dataclass
class QuizQuestion:
    """Represents a single quiz question."""
    question: str
    answer: str
    choices: List[str]
    correct_index: int


class QuizFormatter:
    """
    Handles formatting of quiz questions with proper validation.
    """

    def __init__(self, delimiter: str = "|", shuffle_choices: bool = True):
        """
        Initialize quiz formatter.

        Args:
            delimiter: Delimiter used to separate question parts
            shuffle_choices: Whether to shuffle answer choices
        """
        self.delimiter = delimiter
        self.shuffle_choices = shuffle_choices
        self.logger = logging.getLogger(__name__)

    def _validate_input(self, questions: str) -> None:
        """Validate input questions string."""
        if not questions or not questions.strip():
            raise ValidationError("Questions string cannot be empty")

    def _clean_text_list(self, text_list: List[str]) -> List[str]:
        """Clean and filter a list of text lines."""
        return [line.strip() for line in text_list if line.strip()]

    def _validate_question_parts(self, parts: List[str], question_index: int) -> None:
        """Validate parts of a single question."""
        if len(parts) < 2:
            raise ValidationError(f"Question {question_index} must have at least question text and one answer")

        if not parts[0].strip():
            raise ValidationError(f"Question {question_index} cannot be empty")

        if len(parts) < 5:
            self.logger.warning(f"Question {question_index} has fewer than 4 choices: {len(parts) - 1} choices")

    def _format_single_question(self, question_text: str, question_index: int) -> QuizQuestion:
        """Format a single question from text."""
        parts = [part.strip() for part in question_text.split(self.delimiter)]
        self._validate_question_parts(parts, question_index)

        question = parts[0]
        correct_answer = parts[1]
        choices = parts[1:]  # Include correct answer in choices

        # Clean choices
        choices = self._clean_text_list(choices)
        if not choices:
            raise ValidationError(f"Question {question_index} has no valid choices")

        # Shuffle choices if requested
        if self.shuffle_choices:
            random.shuffle(choices)

        # Find correct answer index
        try:
            correct_index = choices.index(correct_answer)
        except ValueError:
            # If correct answer was removed during cleaning, use first choice
            self.logger.warning(f"Correct answer not found in choices for question {question_index}")
            correct_index = 0

        return QuizQuestion(
            question=question,
            answer=correct_answer,
            choices=choices,
            correct_index=correct_index
        )

    def format_questions(self, questions: str) -> Dict[str, Dict[str, Any]]:
        """
        Format raw questions text into structured data.

        Args:
            questions: Raw questions text with delimiter-separated parts

        Returns:
            Dictionary of formatted questions

        Raises:
            ValidationError: If input validation fails
            QuizFormatError: If formatting fails
        """
        try:
            self._validate_input(questions)

            # Split into lines and clean
            lines = questions.split('\n')
            clean_lines = self._clean_text_list(lines)

            if not clean_lines:
                raise ValidationError("No valid questions found in input")

            self.logger.info(f"Formatting {len(clean_lines)} questions")

            formatted_questions = {}
            failed_questions = []

            for index, line in enumerate(clean_lines):
                try:
                    quiz_question = self._format_single_question(line, index)
                    formatted_questions[str(index)] = {
                        "QUESTION": quiz_question.question,
                        "ANSWER": quiz_question.correct_index,
                        "CHOICES": quiz_question.choices
                    }
                except Exception as e:
                    self.logger.error(f"Failed to format question {index}: {e}")
                    failed_questions.append(index)
                    continue

            if not formatted_questions:
                raise QuizFormatError("No questions were successfully formatted")

            if failed_questions:
                self.logger.warning(f"Failed to format {len(failed_questions)} questions: {failed_questions}")

            self.logger.info(f"Successfully formatted {len(formatted_questions)} questions")
            return formatted_questions

        except Exception as e:
            self.logger.error(f"Failed to format questions: {e}")
            raise QuizFormatError(f"Quiz formatting failed: {e}")

    def format_to_json(self, questions: str, indent: int = 2) -> str:
        """
        Format questions and return as JSON string.

        Args:
            questions: Raw questions text
            indent: JSON indentation level

        Returns:
            JSON string of formatted questions
        """
        formatted_data = self.format_questions(questions)
        return json.dumps(formatted_data, indent=indent, ensure_ascii=False)

    def save_to_file(self, questions: str, output_path: str) -> None:
        """
        Format questions and save to file.

        Args:
            questions: Raw questions text
            output_path: Path to save the formatted JSON
        """
        try:
            json_data = self.format_to_json(questions)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(json_data)

            self.logger.info(f"Saved formatted quiz to: {output_path}")

        except Exception as e:
            self.logger.error(f"Failed to save quiz to file: {e}")
            raise QuizFormatError(f"Failed to save quiz: {e}")


# Backward compatibility function
def format_question(questions: str, delimiter: Optional[str] = None) -> str:
    """
    Legacy function for backward compatibility.

    Args:
        questions: Raw questions text
        delimiter: Optional delimiter (falls back to environment variable)

    Returns:
        JSON string of formatted questions
    """
    import os
    from dotenv import load_dotenv
    load_dotenv(override=True)

    # Use provided delimiter or fall back to environment variable
    actual_delimiter = delimiter or os.getenv('DELIMETER', '|')

    formatter = QuizFormatter(delimiter=actual_delimiter)
    return formatter.format_to_json(questions)


if __name__ == "__main__":
    # Example usage
    quiz = """
question: What is 123 × 456? | 56088 | 55088 | 57088 | 54088
question: What is 234 × 567? | 132678 | 131678 | 133678 | 130678
question: What is 345 × 678? | 233910 | 232910 | 234910 | 231910
question: What is 456 × 789? | 359784 | 358784 | 360784 | 357784
question: What is 567 × 891? | 505197 | 504197 | 506197 | 503197
question: What is 678 × 912? | 618336 | 617336 | 619336 | 616336
question: What is 789 × 123? | 97047 | 96047 | 98047 | 95047
question: What is 891 × 234? | 208494 | 207494 | 209494 | 206494
question: What is 912 × 345? | 314640 | 313640 | 315640 | 312640
question: What is 123 × 789? | 97047 | 96047 | 98047 | 95047
"""

    # Format with default settings
    formatted = format_question(questions=quiz)
    print("Default formatting:")
    print(formatted)

    # Format with custom formatter
    formatter = QuizFormatter(delimiter="|", shuffle_choices=True)
    structured_data = formatter.format_questions(questions)
    print(f"\nStructured data: {len(structured_data)} questions")

    # Test validation
    try:
        formatter.format_questions("")
    except ValidationError as e:
        print(f"\nValidation error caught: {e}")