"""
Java programming benchmark prompt generator with challenging complex problems.
"""
from typing import Dict, List, Tuple, Optional
from ..base import BaseBenchmarkGenerator, BenchmarkPrompt


class JavaBenchmark(BaseBenchmarkGenerator):
    """Java programming benchmark generator focused on challenging complex problems."""

    def __init__(self):
        super().__init__("Java")
        self._setup_templates()

    # Topic-specific methods for direct access
    def object_oriented_programming(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for object-oriented programming topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for object-oriented programming
        """
        return self.generate_benchmark_prompt('object_oriented_programming', question_count, **kwargs)

    def data_structures(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for data structures topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for data structures
        """
        return self.generate_benchmark_prompt('data_structures', question_count, **kwargs)

    def algorithms(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for algorithms topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for algorithms
        """
        return self.generate_benchmark_prompt('algorithms', question_count, **kwargs)

    def multithreading(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for multithreading topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for multithreading
        """
        return self.generate_benchmark_prompt('multithreading', question_count, **kwargs)

    def file_io(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for file I/O topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for file I/O
        """
        return self.generate_benchmark_prompt('file_io', question_count, **kwargs)

    def exception_handling(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for exception handling topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for exception handling
        """
        return self.generate_benchmark_prompt('exception_handling', question_count, **kwargs)

    def collections_framework(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for collections framework topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for collections framework
        """
        return self.generate_benchmark_prompt('collections_framework', question_count, **kwargs)

    def java_8_features(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for Java 8 features topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for Java 8 features
        """
        return self.generate_benchmark_prompt('java_8_features', question_count, **kwargs)

    def design_patterns(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for design patterns topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for design patterns
        """
        return self.generate_benchmark_prompt('design_patterns', question_count, **kwargs)

    def java_standard_library(self, question_count: int = 10, **kwargs) -> BenchmarkPrompt:
        """Generate benchmark prompt for Java standard library topic.

        Args:
            question_count: Number of questions to generate (default: 10)
            **kwargs: Additional parameters for template customization

        Returns:
            BenchmarkPrompt for Java standard library
        """
        return self.generate_benchmark_prompt('java_standard_library', question_count, **kwargs)

    def _setup_templates(self) -> None:
        """Set up Java programming topic templates."""
        self.topic_templates = {
            'object_oriented_programming': {
                'user': """
Generate {quantity} challenging object-oriented programming problems.
Include problems involving:
- Complex class hierarchies and inheritance relationships
- Polymorphism and dynamic binding scenarios
- Abstract classes and interfaces with multiple implementations
- Design patterns and their practical applications
- Code refactoring and object-oriented design principles

Grade level: Advanced undergraduate/college level
Focus on problems requiring deep understanding of OOP concepts and design patterns.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in object-oriented programming and software design.

Create sophisticated OOP problems that test advanced understanding of object-oriented principles.
Ensure all problems reflect current best practices and real-world applications.
Include problems that demonstrate the importance of proper OOP design in software development.
Use accurate programming concepts and appropriate coding scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include multiple OOP concepts and their interactions
- Emphasize design principles and best practices
- Provide distractors that test common OOP misconceptions
"""
            },
            'data_structures': {
                'user': """
Generate {quantity} advanced data structures problems.
Include problems involving:
- Complex tree structures and traversal algorithms
- Graph implementations and path-finding algorithms
- Hash table design and collision resolution strategies
- Dynamic data structures and memory management
- Data structure selection and performance analysis

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of data structure implementation and analysis.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in data structures and algorithm analysis.

Create challenging data structure problems that test advanced understanding of abstract data types.
Ensure all problems reflect current computer science theory and practical applications.
Include problems that demonstrate the importance of proper data structure selection.
Use accurate computational complexity analysis and appropriate implementation scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include multiple data structures and their comparative analysis
- Emphasize time and space complexity considerations
- Provide distractors that test common data structure misconceptions
"""
            },
            'algorithms': {
                'user': """
Generate {quantity} challenging algorithm problems.
Include problems involving:
- Complex sorting and searching algorithm implementations
- Dynamic programming and optimization techniques
- Divide and conquer strategies and their applications
- Greedy algorithms and their correctness proofs
- Algorithm analysis and performance optimization

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of algorithm design and analysis.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in algorithms and computational theory.

Create sophisticated algorithm problems that test advanced understanding of computational problem-solving.
Ensure all problems reflect current algorithmic theory and best practices.
Include problems that demonstrate the importance of efficient algorithm design.
Use accurate computational complexity analysis and appropriate problem scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include multiple algorithmic approaches and their comparisons
- Emphasize correctness, efficiency, and optimality considerations
- Provide distractors that test common algorithmic misconceptions
"""
            },
            'multithreading': {
                'user': """
Generate {quantity} advanced multithreading problems.
Include problems involving:
- Complex thread synchronization and deadlock scenarios
- Concurrent data structures and thread safety
- Thread pools and executor service implementations
- Producer-consumer problems and resource sharing
- Performance optimization and scalability considerations

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of concurrent programming concepts.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in concurrent programming and multithreading.

Create challenging multithreading problems that test advanced understanding of concurrent execution.
Ensure all problems reflect current best practices in concurrent programming.
Include problems that demonstrate the complexity of thread synchronization and coordination.
Use accurate concurrency concepts and appropriate parallel computing scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include synchronization mechanisms and their proper usage
- Emphasize thread safety and performance considerations
- Provide distractors that test common concurrency misconceptions
"""
            },
            'file_io': {
                'user': """
Generate {quantity} challenging file I/O problems.
Include problems involving:
- Complex file processing and data parsing scenarios
- Binary file handling and serialization techniques
- Stream-based processing and memory efficiency
- Error handling and resource management
- Performance optimization for large-scale data processing

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of file systems and data persistence.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in file systems and data persistence.

Create sophisticated file I/O problems that test advanced understanding of data handling and storage.
Ensure all problems reflect current best practices in file processing and resource management.
Include problems that demonstrate the importance of efficient data processing techniques.
Use accurate file system concepts and appropriate real-world data scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include various file formats and processing strategies
- Emphasize efficiency, reliability, and error handling
- Provide distractors that test common file I/O misconceptions
"""
            },
            'exception_handling': {
                'user': """
Generate {quantity} advanced exception handling problems.
Include problems involving:
- Complex exception hierarchies and custom exception creation
- Exception propagation and handling strategies
- Resource management and try-with-resources patterns
- Debugging and error recovery scenarios
- Best practices in exception design and usage

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of robust error handling and program reliability.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in software reliability and error handling.

Create challenging exception handling problems that test advanced understanding of program robustness.
Ensure all problems reflect current best practices in exception handling and error recovery.
Include problems that demonstrate the importance of proper error management in software.
Use accurate exception handling concepts and appropriate failure scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include exception hierarchies and handling strategies
- Emphasize resource management and program reliability
- Provide distractors that test common exception handling misconceptions
"""
            },
            'collections_framework': {
                'user': """
Generate {quantity} challenging collections framework problems.
Include problems involving:
- Complex collection selection and usage scenarios
- Custom comparator implementations and sorting strategies
- Collection views and concurrent modification handling
- Performance optimization and memory considerations
- Stream API and functional programming with collections

Grade level: Advanced undergraduate/college level
Focus on problems requiring deep understanding of Java Collections Framework.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in Java Collections Framework and functional programming.

Create sophisticated collections problems that test advanced understanding of data manipulation in Java.
Ensure all problems reflect current best practices in collection usage and functional programming.
Include problems that demonstrate the versatility of Java's collection system.
Use accurate collection concepts and appropriate real-world data scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include various collection types and their appropriate usage
- Emphasize performance, thread safety, and functional approaches
- Provide distractors that test common collections misconceptions
"""
            },
            'java_8_features': {
                'user': """
Generate {quantity} advanced Java 8 features problems.
Include problems involving:
- Complex lambda expressions and functional interfaces
- Stream API operations and parallel processing
- Optional usage and null safety patterns
- Method references and constructor references
- Date and time API improvements

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of modern Java features and functional programming.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in modern Java features and functional programming.

Create challenging Java 8 problems that test advanced understanding of functional programming concepts.
Ensure all problems reflect current best practices in functional programming and modern Java.
Include problems that demonstrate the power of functional approaches in Java.
Use accurate functional programming concepts and appropriate modern Java scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include multiple Java 8 features and their interactions
- Emphasize functional programming benefits and best practices
- Provide distractors that test common modern Java misconceptions
"""
            },
            'design_patterns': {
                'user': """
Generate {quantity} advanced design patterns problems.
Include problems involving:
- Complex scenarios requiring multiple design patterns
- Pattern selection and implementation trade-offs
- Gang of Four patterns and their modern applications
- Anti-patterns and common design mistakes
- Software architecture and design principles

Grade level: Advanced undergraduate/college level
Focus on problems requiring understanding of software design patterns and architecture.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in software design patterns and architecture.

Create sophisticated design pattern problems that test advanced understanding of software architecture.
Ensure all problems reflect current best practices in software design and pattern usage.
Include problems that demonstrate the importance of proper software design.
Use accurate design pattern concepts and appropriate real-world scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include multiple design patterns and their applications
- Emphasize design principles and architectural considerations
- Provide distractors that test common design pattern misconceptions
"""
            },
            'java_standard_library': {
                'user': """
Generate {quantity} challenging Java Standard Library problems.
Include problems involving:
- Complex utility class usage and best practices
- Reflection and dynamic programming scenarios
- Internationalization and localization challenges
- Security and cryptography API usage
- Performance optimization with standard library features

Grade level: Advanced undergraduate/college level
Focus on problems requiring deep understanding of Java Standard Library capabilities.
Include both theoretical concepts and practical implementation challenges.

Output format for each question:
question_text | correct_answer | incorrect1 | incorrect2 | incorrect3
""",
                'system': """
You are an expert computer science educator specializing in Java Standard Library and enterprise development.

Create challenging standard library problems that test advanced understanding of Java's built-in capabilities.
Ensure all problems reflect current best practices in standard library usage.
Include problems that demonstrate the power and versatility of Java's standard library.
Use accurate library concepts and appropriate enterprise-level scenarios.

Requirements:
- Generate exactly {quantity} questions
- Each question must have exactly 4 answer choices
- Problems should challenge advanced programming students
- Include various standard library packages and their features
- Emphasize best practices and performance optimization
- Provide distractors that test common standard library misconceptions
"""
            }
        }

    def _get_topic_templates(self, topic: str) -> Tuple[str, str]:
        """Get templates for a specific topic."""
        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in self.topic_templates:
            templates = self.topic_templates[topic_lower]
            return templates['user'], templates['system']
        else:
            available_topics = list(self.topic_templates.keys())
            raise ValueError(f"Topic '{topic}' not found. Available topics: {available_topics}")

    def _get_grading_criteria(self, topic: str) -> List[str]:
        """Get specific grading criteria for Java programming topics."""
        base_criteria = [
            "Programming accuracy and precision",
            "Clear problem statement with unambiguous requirements",
            "Appropriate difficulty level for advanced programming students",
            "Educational relevance and real-world applications",
            "Single unambiguous correct answer",
            "Plausible distractors reflecting common misconceptions"
        ]

        topic_specific = {
            'object_oriented_programming': ["Understanding of OOP principles and design patterns"],
            'data_structures': ["Knowledge of data structure implementation and analysis"],
            'algorithms': ["Understanding of algorithm design and complexity analysis"],
            'multithreading': ["Knowledge of concurrent programming and thread safety"],
            'file_io': ["Understanding of file systems and data persistence"],
            'exception_handling': ["Knowledge of error handling and program reliability"],
            'collections_framework': ["Understanding of Java Collections and functional programming"],
            'java_8_features': ["Knowledge of modern Java features and functional programming"],
            'design_patterns': ["Understanding of software design patterns and architecture"],
            'java_standard_library': ["Knowledge of Java Standard Library and enterprise development"]
        }

        topic_lower = topic.lower().replace(' ', '_')
        if topic_lower in topic_specific:
            return base_criteria + topic_specific[topic_lower]
        return base_criteria

    def list_topics(self) -> List[str]:
        """List all available Java programming topics."""
        return [
            "Object-Oriented Programming",
            "Data Structures",
            "Algorithms",
            "Multithreading",
            "File I/O",
            "Exception Handling",
            "Collections Framework",
            "Java 8 Features",
            "Design Patterns",
            "Java Standard Library"
        ]