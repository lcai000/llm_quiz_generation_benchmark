"""
Test runner script for the LLM Quiz Generation Benchmark.
"""
import unittest
import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def run_tests():
    """Run all tests in the tests directory."""
    # Discover and run all tests
    loader = unittest.TestLoader()
    test_dir = project_root / "tests"
    suite = loader.discover(str(test_dir), pattern="test_*.py")

    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return exit code based on test results
    return 0 if result.wasSuccessful() else 1

def run_specific_test(test_name):
    """Run a specific test module."""
    loader = unittest.TestLoader()
    test_dir = project_root / "tests"

    try:
        suite = loader.loadTestsFromName(f"tests.{test_name}")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return 0 if result.wasSuccessful() else 1
    except ImportError:
        print(f"Test module '{test_name}' not found.")
        print("Available test modules:")
        for test_file in test_dir.glob("test_*.py"):
            print(f"  - {test_file.stem}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific test
        test_name = sys.argv[1]
        exit_code = run_specific_test(test_name)
    else:
        # Run all tests
        exit_code = run_tests()

    sys.exit(exit_code)