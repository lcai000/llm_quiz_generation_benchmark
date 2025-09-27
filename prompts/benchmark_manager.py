"""
Central benchmark manager for coordinating all subject prompt generation.
"""
import logging
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import json
from pathlib import Path

from .base import BenchmarkPrompt, BaseBenchmarkGenerator
from .math.algebra import AlgebraBenchmark
from .math.precalculus import PrecalculusBenchmark
from .science.biology import BiologyBenchmark
from .science.chemistry import ChemistryBenchmark
from .history.us_history import USHistoryBenchmark
from .history.world_history import WorldHistoryBenchmark
from .programming.java import JavaBenchmark


@dataclass
class BenchmarkSuite:
    """Represents a collection of benchmark prompts for testing."""
    name: str
    prompts: List[BenchmarkPrompt]
    metadata: Dict[str, Any]


class BenchmarkManager:
    """
    Central manager for all benchmark prompt generation and coordination.
    """

    def __init__(self):
        """Initialize the benchmark manager."""
        self.logger = logging.getLogger(__name__)
        self.subjects = self._initialize_subjects()
        self.benchmark_suites = {}

        self.logger.info(f"Initialized BenchmarkManager with {len(self.subjects)} subjects")

    def _initialize_subjects(self) -> Dict[str, BaseBenchmarkGenerator]:
        """Initialize all subject benchmark generators."""
        return {
            'algebra': AlgebraBenchmark(),
            'precalculus': PrecalculusBenchmark(),
            'biology': BiologyBenchmark(),
            'chemistry': ChemistryBenchmark(),
            'us_history': USHistoryBenchmark(),
            'world_history': WorldHistoryBenchmark(),
            'java': JavaBenchmark()
        }

    def list_subjects(self) -> List[str]:
        """List all available subjects."""
        return list(self.subjects.keys())

    def get_subject(self, subject: str) -> Optional[BaseBenchmarkGenerator]:
        """Get a specific subject benchmark generator."""
        return self.subjects.get(subject.lower())

    def list_subject_topics(self, subject: str) -> List[str]:
        """List all topics for a specific subject."""
        generator = self.subjects.get(subject.lower())
        return generator.list_topics() if generator else []

    def generate_single_prompt(self, subject: str, topic: str, question_count: int = 10) -> Optional[BenchmarkPrompt]:
        """Generate a single benchmark prompt."""
        generator = self.subjects.get(subject.lower())
        if generator:
            try:
                return generator.generate_benchmark_prompt(topic, question_count)
            except Exception as e:
                self.logger.error(f"Failed to generate prompt for {subject}/{topic}: {e}")
                return None
        return None

    def generate_subject_benchmark(self, subject: str, questions_per_topic: int = 5) -> BenchmarkSuite:
        """Generate a comprehensive benchmark for a subject."""
        generator = self.subjects.get(subject.lower())
        if not generator:
            raise ValueError(f"Subject '{subject}' not found")

        prompts = generator.generate_comprehensive_benchmark(questions_per_topic)
        suite = BenchmarkSuite(
            name=f"{subject.title()} Comprehensive Benchmark",
            prompts=prompts,
            metadata={
                'subject': subject,
                'total_questions': sum(p.question_count for p in prompts),
                'topics_covered': len(prompts),
                'difficulty_level': 'Challenging High School'
            }
        )

        self.benchmark_suites[subject.lower()] = suite
        self.logger.info(f"Generated {subject} benchmark with {len(prompts)} topic prompts")

        return suite

    def generate_comprehensive_benchmark(self, questions_per_topic: int = 3) -> BenchmarkSuite:
        """Generate a comprehensive benchmark covering all subjects."""
        all_prompts = []
        total_questions = 0
        subjects_covered = []

        for subject_name, generator in self.subjects.items():
            try:
                prompts = generator.generate_comprehensive_benchmark(questions_per_topic)
                all_prompts.extend(prompts)
                total_questions += sum(p.question_count for p in prompts)
                subjects_covered.append(subject_name)
                self.logger.info(f"Added {len(prompts)} prompts from {subject_name}")
            except Exception as e:
                self.logger.error(f"Failed to generate prompts for {subject_name}: {e}")

        suite = BenchmarkSuite(
            name="Comprehensive LLM Benchmark Suite",
            prompts=all_prompts,
            metadata={
                'total_subjects': len(subjects_covered),
                'total_questions': total_questions,
                'total_prompts': len(all_prompts),
                'subjects_covered': subjects_covered,
                'difficulty_level': 'Challenging High School',
                'benchmark_type': 'comprehensive'
            }
        )

        self.benchmark_suites['comprehensive'] = suite
        self.logger.info(f"Generated comprehensive benchmark with {len(all_prompts)} total prompts")

        return suite

    def generate_targeted_benchmark(self, subjects: List[str], topics: Dict[str, List[str]],
                                  questions_per_topic: int = 5) -> BenchmarkSuite:
        """Generate a targeted benchmark for specific subjects and topics."""
        all_prompts = []
        total_questions = 0

        for subject in subjects:
            generator = self.subjects.get(subject.lower())
            if not generator:
                self.logger.warning(f"Subject '{subject}' not found, skipping")
                continue

            subject_topics = topics.get(subject, [])
            if not subject_topics:
                # Generate for all topics in subject
                try:
                    prompts = generator.generate_comprehensive_benchmark(questions_per_topic)
                    all_prompts.extend(prompts)
                    total_questions += sum(p.question_count for p in prompts)
                except Exception as e:
                    self.logger.error(f"Failed to generate prompts for {subject}: {e}")
            else:
                # Generate for specific topics
                for topic in subject_topics:
                    try:
                        prompt = generator.generate_benchmark_prompt(topic, questions_per_topic)
                        if prompt:
                            all_prompts.append(prompt)
                            total_questions += prompt.question_count
                    except Exception as e:
                        self.logger.error(f"Failed to generate prompt for {subject}/{topic}: {e}")

        suite = BenchmarkSuite(
            name="Targeted LLM Benchmark Suite",
            prompts=all_prompts,
            metadata={
                'target_subjects': subjects,
                'total_questions': total_questions,
                'total_prompts': len(all_prompts),
                'difficulty_level': 'Challenging High School',
                'benchmark_type': 'targeted'
            }
        )

        return suite

    def get_benchmark_suite(self, name: str) -> Optional[BenchmarkSuite]:
        """Retrieve a previously generated benchmark suite."""
        return self.benchmark_suites.get(name.lower())

    def list_benchmark_suites(self) -> List[str]:
        """List all available benchmark suites."""
        return list(self.benchmark_suites.keys())

    def export_benchmark_suite(self, suite_name: str, output_path: str) -> str:
        """Export a benchmark suite to JSON file."""
        suite = self.get_benchmark_suite(suite_name)
        if not suite:
            raise ValueError(f"Benchmark suite '{suite_name}' not found")

        export_data = {
            'name': suite.name,
            'metadata': suite.metadata,
            'prompts': [
                {
                    'subject': prompt.subject,
                    'topic': prompt.topic,
                    'expected_difficulty': prompt.expected_difficulty,
                    'question_count': prompt.question_count,
                    'quality_metrics': prompt.quality_metrics,
                    'user_prompt': prompt.user_prompt,
                    'system_prompt': prompt.system_prompt
                }
                for prompt in suite.prompts
            ]
        }

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)

            self.logger.info(f"Exported benchmark suite '{suite_name}' to {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"Failed to export benchmark suite: {e}")
            raise

    def import_benchmark_suite(self, file_path: str) -> str:
        """Import a benchmark suite from JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Recreate benchmark suite
            prompts = []
            for prompt_data in data['prompts']:
                prompt = BenchmarkPrompt(
                    user_prompt=prompt_data['user_prompt'],
                    system_prompt=prompt_data['system_prompt'],
                    subject=prompt_data['subject'],
                    topic=prompt_data['topic'],
                    expected_difficulty=prompt_data['expected_difficulty'],
                    question_count=prompt_data['question_count'],
                    quality_metrics=prompt_data['quality_metrics']
                )
                prompts.append(prompt)

            suite = BenchmarkSuite(
                name=data['name'],
                prompts=prompts,
                metadata=data['metadata']
            )

            suite_name = suite.name.lower().replace(' ', '_')
            self.benchmark_suites[suite_name] = suite

            self.logger.info(f"Imported benchmark suite '{suite.name}' from {file_path}")
            return suite_name

        except Exception as e:
            self.logger.error(f"Failed to import benchmark suite: {e}")
            raise

    def get_benchmark_statistics(self, suite_name: str) -> Dict[str, Any]:
        """Get detailed statistics about a benchmark suite."""
        suite = self.get_benchmark_suite(suite_name)
        if not suite:
            raise ValueError(f"Benchmark suite '{suite_name}' not found")

        stats = {
            'name': suite.name,
            'total_prompts': len(suite.prompts),
            'total_questions': sum(p.question_count for p in suite.prompts),
            'subjects': {}
        }

        # Subject breakdown
        for prompt in suite.prompts:
            subject = prompt.subject
            if subject not in stats['subjects']:
                stats['subjects'][subject] = {
                    'prompt_count': 0,
                    'question_count': 0,
                    'topics': set()
                }

            stats['subjects'][subject]['prompt_count'] += 1
            stats['subjects'][subject]['question_count'] += prompt.question_count
            stats['subjects'][subject]['topics'].add(prompt.topic)

        # Convert sets to lists for JSON serialization
        for subject_data in stats['subjects'].values():
            subject_data['topics'] = list(subject_data['topics'])

        return stats

    def create_benchmark_report(self, suite_name: str) -> str:
        """Create a human-readable benchmark report."""
        stats = self.get_benchmark_statistics(suite_name)
        suite = self.get_benchmark_suite(suite_name)

        report = f"""
# {suite.name} Benchmark Report

## Overview
- Total Prompts: {stats['total_prompts']}
- Total Questions: {stats['total_questions']}
- Difficulty Level: {suite.metadata.get('difficulty_level', 'Unknown')}

## Subject Breakdown
"""

        for subject, data in stats['subjects'].items():
            report += f"""
### {subject.title()}
- Prompts: {data['prompt_count']}
- Questions: {data['question_count']}
- Topics: {', '.join(data['topics'])}
"""

        report += f"""
## Generated: {suite.metadata.get('generated_date', 'Unknown')}
"""

        return report


# Global benchmark manager instance
benchmark_manager = BenchmarkManager()