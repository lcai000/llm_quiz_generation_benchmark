"""
Benchmark system for LLM quiz generation with improved error handling and logging.
"""
import json
import logging
from typing import Dict, Any, Optional
from pathlib import Path

from llm_framework import GeminiClient, ConfigurationError, APIError
from prompts import Math
from quiz_format import format_question


class QuizGenerator:
    """
    Handles quiz generation using the new Gemini client.
    """

    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None, api_url: Optional[str] = None):
        """
        Initialize quiz generator.

        Args:
            api_key: Gemini API key (falls back to environment variable)
            model_name: Model name (falls back to environment variable)
            api_url: API URL (falls back to environment variable)
        """
        self.client = GeminiClient(api_key, model_name, api_url)
        self.model_name = model_name or self.client.model_name

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def generate_quiz_batch(self, prompt: str, system_prompt: Optional[str] = None, max_tokens: Optional[int] = None) -> str:
        """
        Generate a batch of quiz questions.

        Args:
            prompt: User prompt for quiz generation
            system_prompt: Optional system prompt
            max_tokens: Optional maximum tokens

        Returns:
            Generated quiz text

        Raises:
            ConfigurationError: If API configuration is invalid
            APIError: If API call fails
        """
        try:
            self.logger.info(f"Generating quiz batch with model: {self.model_name}")
            self.logger.debug(f"Prompt length: {len(prompt)} characters")

            response = self.client.generate_response(
                prompt=prompt,
                system_prompt=system_prompt,
                max_tokens=max_tokens
            )

            self.logger.info(f"Successfully generated quiz batch")
            self.logger.debug(f"Response length: {len(response)} characters")

            return response

        except (ConfigurationError, APIError) as e:
            self.logger.error(f"Failed to generate quiz batch: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error in quiz generation: {e}")
            raise APIError(f"Quiz generation failed: {e}")


class QuizBenchmark:
    """
    Main benchmark system for generating and evaluating quizzes.
    """

    def __init__(self, generator: Optional[QuizGenerator] = None, output_dir: str = "results"):
        """
        Initialize quiz benchmark.

        Args:
            generator: Quiz generator instance
            output_dir: Directory to save results
        """
        self.generator = generator or QuizGenerator()
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

        # Set up logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def run_benchmark(self, batch_size: int, batches: int, prompt: str, system_prompt: str) -> Dict[str, Any]:
        """
        Run quiz generation benchmark.

        Args:
            batch_size: Number of questions per batch
            batches: Number of batches to generate
            prompt: User prompt for quiz generation
            system_prompt: System prompt for quiz generation

        Returns:
            Benchmark results dictionary
        """
        try:
            self.logger.info(f"Starting benchmark: {batches} batches of {batch_size} questions each")
            self.logger.info(f"Total questions to generate: {batch_size * batches}")

            quiz_text = ""
            successful_batches = 0

            for batch in range(batches):
                try:
                    self.logger.info(f"Generating batch {batch + 1}/{batches}")
                    batch_result = self.generator.generate_quiz_batch(
                        prompt=prompt,
                        system_prompt=system_prompt
                    )

                    if batch_result:
                        quiz_text += '\n' + batch_result + '\n'
                        successful_batches += 1
                        self.logger.info(f"Successfully generated batch {batch + 1}")
                    else:
                        self.logger.warning(f"Batch {batch + 1} returned empty result")

                except Exception as e:
                    self.logger.error(f"Failed to generate batch {batch + 1}: {e}")
                    continue

            if not quiz_text.strip():
                raise APIError("No quiz content was generated")

            # Format the quiz
            self.logger.info("Formatting quiz questions")
            formatted_quiz = format_question(questions=quiz_text)

            # Prepare results
            total_questions = batch_size * batches
            results = {
                "MODEL": self.generator.model_name,
                "QUANTITY": total_questions,
                "BATCH_SIZE": batch_size,
                "SUCCESSFUL_BATCHES": successful_batches,
                "SUCCESS_RATE": successful_batches / batches if batches > 0 else 0,
                "QUIZ": formatted_quiz
            }

            self.logger.info(f"Benchmark completed successfully")
            self.logger.info(f"Success rate: {results['SUCCESS_RATE']:.2%}")

            return results

        except Exception as e:
            self.logger.error(f"Benchmark failed: {e}")
            raise

    def save_results(self, results: Dict[str, Any], filename: Optional[str] = None) -> str:
        """
        Save benchmark results to file.

        Args:
            results: Benchmark results dictionary
            filename: Optional filename (auto-generated if not provided)

        Returns:
            Path to saved file
        """
        if filename is None:
            timestamp = json.dumps(results.get("MODEL", "unknown")).strip('"')
            filename = f"benchmark_results_{timestamp}.json"

        output_path = self.output_dir / filename

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)

            self.logger.info(f"Results saved to: {output_path}")
            return str(output_path)

        except Exception as e:
            self.logger.error(f"Failed to save results: {e}")
            raise


def main():
    """Main function for running the benchmark."""
    try:
        # Initialize prompt generator
        math_prompt = Math()
        math_prompt.quantity = 10

        # Get multiplication quiz prompts
        quiz_prompts = math_prompt.multiplication()
        user_prompt = quiz_prompts["user_prompt"]
        system_prompt = quiz_prompts["system_prompt"]

        # Initialize benchmark
        benchmark = QuizBenchmark()

        # Run benchmark
        results = benchmark.run_benchmark(
            batch_size=10,
            batches=3,
            prompt=user_prompt,
            system_prompt=system_prompt
        )

        # Save results
        output_file = benchmark.save_results(results, "example_result.json")

        # Print results
        print("\n=== BENCHMARK RESULTS ===")
        print(f"Model: {results['MODEL']}")
        print(f"Total Questions: {results['QUANTITY']}")
        print(f"Batch Size: {results['BATCH_SIZE']}")
        print(f"Successful Batches: {results['SUCCESSFUL_BATCHES']}")
        print(f"Success Rate: {results['SUCCESS_RATE']:.2%}")
        print(f"Results saved to: {output_file}")
        print("========================\n")

        return results

    except Exception as e:
        logging.error(f"Benchmark execution failed: {e}")
        return None


if __name__ == "__main__":
    main()