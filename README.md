# LLM Quiz Generation Benchmark

A professional framework for benchmarking Large Language Models' ability to generate educational quizzes, specifically focused on mathematics. This system provides a robust, scalable, and well-tested solution for evaluating LLM performance in educational content generation.

## Features

- **Gemini API Integration**: Clean interface for Google's Gemini API
- **Comprehensive Error Handling**: Robust error handling and logging throughout
- **Modular Architecture**: Clean separation of concerns with dedicated modules
- **Input Validation**: Type hints and validation throughout the codebase
- **Quiz Formatting**: Intelligent quiz question formatting with answer shuffling
- **Prompt Generation**: Template-based prompt generation system
- **Benchmarking**: Built-in benchmarking with success rate tracking
- **Unit Tests**: Comprehensive test coverage
- **Backward Compatibility**: Maintains compatibility with existing code

## Project Structure

```
llm_quiz_generation_benchmark/
├── llm_framework/              # Custom LLM framework
│   ├── __init__.py
│   ├── gemini_client.py       # Gemini API client
│   └── exceptions.py          # Framework exceptions
├── config/                    # Configuration management
│   ├── __init__.py
│   └── settings.py            # Configuration classes
├── utils/                     # Utility functions
│   ├── __init__.py
│   └── logger.py              # Logging utilities
├── tests/                     # Unit tests
│   ├── __init__.py
│   ├── test_llm_framework.py
│   ├── test_quiz_format.py
│   └── test_prompts.py
├── benchmark.py               # Main benchmark system
├── prompts.py                 # Prompt generation
├── quiz_format.py             # Quiz formatting utilities
├── llm_framework.py           # Legacy compatibility layer
├── run_tests.py               # Test runner
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd llm_quiz_generation_benchmark
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Gemini API credentials
```

## Configuration

The system uses environment variables for configuration. Create a `.env` file:

```env
# Gemini API Configuration
LLM_KEY=your_gemini_api_key
LLM_NAME=gemini-2.5-flash-lite
LLM_URL=https://generativelanguage.googleapis.com/v1beta/models/LLM_NAME:generateContent

# Quiz Configuration
DELIMETER=|
BATCH_SIZE=10
QUANTITY=30

# Application Configuration
LOG_LEVEL=INFO
OUTPUT_DIR=results
```

## Usage

### Basic Usage

```python
from benchmark import QuizBenchmark
from prompts import MathQuizGenerator

# Initialize prompt generator
math_gen = MathQuizGenerator()
prompts = math_gen.multiplication(quantity=10, grade_level="4th-5th")

# Run benchmark
benchmark = QuizBenchmark()
results = benchmark.run_benchmark(
    batch_size=10,
    batches=3,
    prompt=prompts["user_prompt"],
    system_prompt=prompts["system_prompt"]
)

# Save results
benchmark.save_results(results, "math_quiz_results.json")
```

### Advanced Usage

```python
from llm_framework import GeminiClient
from quiz_format import QuizFormatter
from prompts import PromptGenerator

# Use the new Gemini client directly
client = GeminiClient()
response = client.generate_response(
    prompt="Generate a 5-question math quiz",
    system_prompt="You are an expert math teacher"
)

# Format the quiz
formatter = QuizFormatter()
formatted_quiz = formatter.format_to_json(response)
```

### Running from Command Line

```bash
# Run all tests
python run_tests.py

# Run specific test module
python run_tests.py test_quiz_format

# Run the main benchmark
python benchmark.py
```

## Testing

The project includes comprehensive unit tests:

```bash
# Run all tests
python run_tests.py

# Run specific test module
python run_tests.py test_llm_framework
python run_tests.py test_quiz_format
python run_tests.py test_prompts

# Run tests with coverage
python -m pytest tests/ --cov=llm_framework --cov=tests --cov-report=html
```

## API Reference

### GeminiClient

```python
client = GeminiClient(api_key, model_name, api_url)
response = client.generate_response(prompt, system_prompt, max_tokens)
```

### QuizFormatter

```python
formatter = QuizFormatter(delimiter="|", shuffle_choices=True)
formatted_data = formatter.format_questions(questions)
json_output = formatter.format_to_json(questions)
```

### QuizBenchmark

```python
benchmark = QuizBenchmark(generator, output_dir)
results = benchmark.run_benchmark(batch_size, batches, prompt, system_prompt)
benchmark.save_results(results, filename)
```

## Error Handling

The framework provides specific exception types:

- `ConfigurationError`: Configuration-related errors
- `APIError`: API call failures
- `ValidationError`: Input validation errors
- `QuizFormatError`: Quiz formatting errors

## Logging

The system includes comprehensive logging:

```python
import logging
logging.basicConfig(level=logging.INFO)

# Logs are automatically written to:
# - Console output
# - results/logs/quiz_benchmark.log
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Examples

### Creating Custom Quiz Types

```python
from prompts import PromptGenerator

generator = PromptGenerator()
prompts = generator.generate_quiz_prompt(
    quantity=15,
    details="Create a science quiz about the solar system for 3rd grade students"
)

# Use with benchmark system
from benchmark import QuizBenchmark
benchmark = QuizBenchmark()
results = benchmark.run_benchmark(
    batch_size=5,
    batches=3,
    prompt=prompts.user_prompt,
    system_prompt=prompts.system_prompt
)
```

### Custom Quiz Formatting

```python
from quiz_format import QuizFormatter

# Custom formatter with different delimiter
formatter = QuizFormatter(delimiter="#", shuffle_choices=False)

# Save directly to file
formatter.save_to_file(quiz_text, "custom_quiz.json")
```

## Performance Considerations

- Use appropriate batch sizes to avoid API rate limits
- Monitor memory usage for large quiz generation tasks
- Leverage the built-in success rate tracking for benchmark analysis
- Consider caching results for repeated evaluations

## Troubleshooting

### Common Issues

1. **API Key Not Found**: Ensure `LLM_KEY` is set in your environment variables
2. **Empty Quiz Results**: Check API response format and system prompts
3. **Formatting Errors**: Verify delimiter consistency in quiz text
4. **Import Errors**: Ensure all dependencies are installed

### Debug Mode

Enable debug logging for detailed output:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Changelog

### Version 1.0.0
- Initial professional release
- Complete framework rewrite with improved error handling
- Added comprehensive unit tests
- Implemented proper configuration management
- Enhanced modularity and maintainability